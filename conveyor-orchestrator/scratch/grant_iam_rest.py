import json
import urllib.request
import urllib.error
import google.auth
from google.auth.transport.requests import Request

def main():
    project_id = "ce-testing-465204"
    member = "serviceAccount:service-526827734705@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
    role = "roles/aiplatform.user"
    
    print("Fetching Google Application Default Credentials (ADC)...")
    credentials, project = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    
    print("Refreshing credentials...")
    credentials.refresh(Request())
    access_token = credentials.token
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    # 1. Get current IAM policy
    get_url = f"https://cloudresourcemanager.googleapis.com/v1/projects/{project_id}:getIamPolicy"
    print(f"Retrieving current IAM policy for project: {project_id}...")
    
    req = urllib.request.Request(get_url, data=b"{}", headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            policy = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error getting IAM policy: {e.code} - {e.read().decode('utf-8')}")
        return
        
    print("Successfully retrieved IAM policy.")
    
    # 2. Update policy bindings
    bindings = policy.get("bindings", [])
    role_binding = None
    for b in bindings:
        if b.get("role") == role:
            role_binding = b
            break
            
    if role_binding is None:
        print(f"Role '{role}' not found in existing bindings. Creating new binding...")
        role_binding = {"role": role, "members": []}
        bindings.append(role_binding)
        
    if member in role_binding["members"]:
        print(f"Member '{member}' already has role '{role}'.")
    else:
        print(f"Adding '{member}' to role '{role}'...")
        role_binding["members"].append(member)
        policy["bindings"] = bindings
        
        # 3. Set updated IAM policy
        set_url = f"https://cloudresourcemanager.googleapis.com/v1/projects/{project_id}:setIamPolicy"
        set_payload = json.dumps({"policy": policy}).encode("utf-8")
        
        set_req = urllib.request.Request(set_url, data=set_payload, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(set_req) as response:
                result = json.loads(response.read().decode("utf-8"))
            print(f"Successfully updated IAM policy! Role '{role}' has been granted to '{member}'.")
        except urllib.error.HTTPError as e:
            print(f"Error setting IAM policy: {e.code} - {e.read().decode('utf-8')}")
            return

if __name__ == "__main__":
    main()
