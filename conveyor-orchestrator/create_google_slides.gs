/**
 * Cymbal Warehouse Automation — Google Slides Generator
 * 
 * Instructions:
 * 1. Open your browser and navigate to: https://script.new
 * 2. Delete any boilerplate code and paste this entire script.
 * 3. Click "Save" (disk icon), then click "Run" (play icon).
 * 4. Authorize Google Apps Script when prompted.
 * 5. Check the Execution log — it will print the direct URL to your new Google Slides deck!
 */

function createCymbalWarehouseSlides() {
  const presentationTitle = "Cymbal Warehouse Automation — Frontier Multi-Agent Fleet";
  const deck = SlidesApp.create(presentationTitle);
  
  // Clean default blank slide
  const slides = deck.getSlides();
  if (slides.length > 0) {
    slides[0].remove();
  }
  
  const COLOR_BG = "#070B14";         // Deep Obsidian
  const COLOR_CARD = "#0E1526";       // Glass Navy
  const COLOR_CYAN = "#00F0FF";       // Neon Cyan
  const COLOR_PURPLE = "#A855F7";     // Electric Purple
  const COLOR_BLUE = "#3B82F6";       // Blue
  const COLOR_PINK = "#EC4899";       // Pink
  const COLOR_EMERALD = "#10B981";    // Emerald Green
  const COLOR_ROSE = "#F43F5E";       // Rose Red
  const COLOR_WHITE = "#FFFFFF";      // Crisp White
  const COLOR_GRAY = "#94A3B8";       // Slate 400
  const COLOR_DARK_GRAY = "#1E293B";  // Slate 800

  function applySlideBackground(slide) {
    slide.getBackground().setSolidFill(COLOR_BG);
  }

  function addSlideHeader(slide, slideNum, title, category) {
    category = category || "CYMBAL WAREHOUSE AUTOMATION // VERTEX AI";
    
    // Category tag
    const catBox = slide.insertTextBox(category + "  •  SLIDE " + ("0" + slideNum).slice(-2) + "/10", 40, 20, 640, 25);
    catBox.getText().getTextStyle().setFontSize(10).setBold(true).setForegroundColor(COLOR_CYAN).setFontFamily("Trebuchet MS");

    // Title
    const titleBox = slide.insertTextBox(title, 40, 42, 640, 45);
    titleBox.getText().getTextStyle().setFontSize(22).setBold(true).setForegroundColor(COLOR_WHITE).setFontFamily("Trebuchet MS");

    // Divider Line
    const line = slide.insertShape(SlidesApp.ShapeType.RECTANGLE, 40, 92, 640, 2);
    line.getFill().setSolidFill(COLOR_DARK_GRAY);
    line.getBorder().getLineFill().setSolidFill(COLOR_DARK_GRAY);
  }

  function addCard(slide, left, top, width, height, title, subtitle, bullets, borderColor, titleColor) {
    borderColor = borderColor || COLOR_CYAN;
    titleColor = titleColor || COLOR_WHITE;

    const shape = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, left, top, width, height);
    shape.getFill().setSolidFill(COLOR_CARD);
    shape.getBorder().getLineFill().setSolidFill(borderColor);
    shape.getBorder().setWeight(1.5);

    const tf = shape.getText();
    tf.setText(title + "\n");
    tf.getTextStyle().setFontFamily("Trebuchet MS");
    
    // Style title
    const titleRange = tf.getRange(0, title.length);
    titleRange.getTextStyle().setFontSize(14).setBold(true).setForegroundColor(titleColor);

    if (subtitle) {
      const startSub = tf.getLength();
      tf.appendText(subtitle.toUpperCase() + "\n\n");
      const subRange = tf.getRange(startSub, tf.getLength());
      subRange.getTextStyle().setFontSize(9).setBold(true).setForegroundColor(borderColor);
    }

    bullets.forEach(function(b) {
      const startB = tf.getLength();
      tf.appendText("•  " + b + "\n\n");
      const bRange = tf.getRange(startB, tf.getLength());
      bRange.getTextStyle().setFontSize(10).setBold(false).setForegroundColor(COLOR_GRAY);
    });
  }

  // ==========================================
  // SLIDE 1: Title Slide
  // ==========================================
  const s1 = deck.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  applySlideBackground(s1);

  const tTag = s1.insertTextBox("GOOGLE CLOUD VERTEX AI  •  ENTERPRISE AGENTIC PLATFORM", 60, 70, 600, 25);
  tTag.getText().getTextStyle().setFontSize(11).setBold(true).setForegroundColor(COLOR_CYAN).setFontFamily("Trebuchet MS");

  const tTitle = s1.insertTextBox("CYMBAL WAREHOUSE AUTOMATION\nAutonomous Multi-Agent Fleet & Industrial Orchestration", 60, 100, 600, 110);
  tTitle.getText().getParagraphs()[0].getRange().getTextStyle().setFontSize(32).setBold(true).setForegroundColor(COLOR_WHITE);
  if (tTitle.getText().getParagraphs().length > 1) {
    tTitle.getText().getParagraphs()[1].getRange().getTextStyle().setFontSize(18).setBold(false).setForegroundColor(COLOR_PURPLE);
  }

  const tSub = s1.insertTextBox("Enterprise Autonomous Operations Powered by the Gemini 3.5+ Multi-Agent Portfolio & GEAP.", 60, 220, 600, 40);
  tSub.getText().getTextStyle().setFontSize(13).setForegroundColor(COLOR_GRAY);

  const modelBadges = [
    { title: "Gemini 3.8 Flash", role: "Fleet Dispatcher & WMS", color: COLOR_CYAN },
    { title: "Gemini 3.5 Flash", role: "Multimodal CCTV Vision", color: COLOR_BLUE },
    { title: "Gemini 3.1 Pro", role: "Deep PLC Diagnostics", color: COLOR_PURPLE },
    { title: "Gemini 3.5 Flash-Lite", role: "High-Volume Telemetry", color: COLOR_PINK }
  ];

  modelBadges.forEach(function(m, idx) {
    const card = s1.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 60 + idx * 152, 275, 142, 70);
    card.getFill().setSolidFill(COLOR_CARD);
    card.getBorder().getLineFill().setSolidFill(m.color);
    card.getBorder().setWeight(1.5);
    const txt = card.getText();
    txt.setText(m.title + "\n" + m.role);
    txt.getParagraphs()[0].getRange().getTextStyle().setFontSize(12).setBold(true).setForegroundColor(COLOR_WHITE);
    if (txt.getParagraphs().length > 1) {
      txt.getParagraphs()[1].getRange().getTextStyle().setFontSize(9).setForegroundColor(m.color);
    }
  });

  // ==========================================
  // SLIDE 2: Keynote Personas & Narrative Arc
  // ==========================================
  const s2 = deck.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  applySlideBackground(s2);
  addSlideHeader(s2, 2, "Keynote Journey: 3 Personas Crossing from Demo to Production", "15-MINUTE EXECUTIVE DEMO  •  CYMBAL INDIA");

  addCard(s2, 40, 110, 205, 250, "Ramesh Yadav", "ACT 1: THE OPERATOR (02:00 - 05:30)", [
    "Lead Operations Specialist (Bhiwandi Hub).",
    "Floor Reality: CV-09 seized with 15 units of SKU-991 trapped.",
    "Live Dashboard: Preset Critical Sensor SKU-991 & Execution DAG.",
    "Autonomous Action: PickerBot-Beta (88% bat) bypass to CV-12.",
    "CXO Value: 90s vs 45m downtime saves ₹15L per peak shift."
  ], COLOR_EMERALD, COLOR_WHITE);

  addCard(s2, 255, 110, 205, 250, "Dr. Ananya Deshmukh", "ACT 2: THE AI HEAD (05:30 - 09:00)", [
    "VP & Head of AI Engineering.",
    "Problem: Zero-trust physical control around 415V equipment.",
    "Live Surface: Threat Matrix & Scorecards (/admin).",
    "Zero-Trust Gate: Blocked interlock bypass (SEC-8821) & DEFCON-2.",
    "Self-Healing: Evals score climb (3.70 ➔ 4.30) via GCP Webhook."
  ], COLOR_PURPLE, COLOR_WHITE);

  addCard(s2, 470, 110, 205, 250, "Rajesh Khurana", "ACT 3: THE CFO CLIMAX (09:00 - 12:30)", [
    "Chief Financial Officer: Custodian of margins across 8.5M daily parcels.",
    "Challenge: Eliminates inference bill shock, maximizes $250K Startup Credits.",
    "Live Surface: Admin Console (/admin) — Cost & Token Reactor with ₹ billing.",
    "Engine: OKF prunes 93% tokens; routes to Gemini 3.5 Flash (< ₹0.04/op).",
    "CXO Value: Traceable unit economics & sustainable AI scale."
  ], COLOR_CYAN, COLOR_WHITE);

  const presBanner = s2.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 40, 370, 635, 30);
  presBanner.getFill().setSolidFill(COLOR_CARD);
  presBanner.getBorder().getLineFill().setSolidFill(COLOR_CYAN);
  presBanner.getBorder().setWeight(1);
  const pTxt = presBanner.getText();
  pTxt.setText("ACT 4 // 12:30 - 15:00 • GRAND FINALE: Google Cloud CE reveals live GEAP, Cloud Run & Vertex AI backend logic.");
  pTxt.getTextStyle().setFontSize(9).setFontFamily("Trebuchet MS").setForegroundColor(COLOR_GRAY);

  // ==========================================
  // SLIDE 3: Problem & Solution
  // ==========================================
  const s3 = deck.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  applySlideBackground(s3);
  addSlideHeader(s3, 3, "From Fragile Siloed Scripts to Autonomous Multi-Agent Intelligence");
  addCard(s3, 40, 110, 310, 250, "The Traditional Bottlenecks", "Fragile & High Human Latency", [
    "Conveyor Jams Trigger Halts: Mechanical jams (E-401) blindside operators, creating backlogs.",
    "Disconnected Silos: WMS, runbooks, and telemetry live in separate consoles.",
    "Dangerous Overrides: Manual motor speed overrides cause bearing fires.",
    "Safety Bypasses: LOTO Level 3 procedures are ignored under operational pressure."
  ], COLOR_ROSE);
  addCard(s3, 370, 110, 310, 250, "The Cymbal Autonomous Fleet", "Unified Multi-Agent System on GEAP", [
    "Automated Bypass Routing: Primary dispatcher coordinates RAG runbooks and AGVs in seconds.",
    "Python Sandbox: Agents write and execute statistical scripts on real sensor dumps.",
    "Multimodal Vision: Real-time CCTV analysis verifies clear conveyor belts.",
    "Zero-Tolerance Safety: Hard refusal of unsafe overrides and automatic LOTO Level 3."
  ], COLOR_CYAN);

  // ==========================================
  // SLIDE 3: Multi-Model Matrix
  // ==========================================
  const s3 = deck.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  applySlideBackground(s3);
  addSlideHeader(s3, 3, "Enterprise Gemini 3.5+ Multi-Model Fleet Architecture");
  addCard(s3, 40, 110, 150, 270, "Gemini 3.8 Flash", "Fleet Dispatcher", [
    "Master Orchestrator",
    "Long-horizon planning",
    "Structured JSON schema",
    "Sub-second latency"
  ], COLOR_CYAN, COLOR_CYAN);
  addCard(s3, 203, 110, 150, 270, "Gemini 3.5 Flash", "CCTV Auditor", [
    "Multimodal Vision",
    "Video frame analysis",
    "Foreign object checks",
    "PPE posture audit"
  ], COLOR_BLUE, COLOR_BLUE);
  addCard(s3, 366, 110, 150, 270, "Gemini 3.1 Pro", "Cognitive Deep Think", [
    "Root-Cause Diagnostician",
    "Physics & thermal math",
    "PLC ladder logic synthesis",
    "LLM-as-Judge Continuous Eval"
  ], COLOR_PURPLE, COLOR_PURPLE);
  addCard(s3, 530, 110, 150, 270, "Gemini 3.5 Flash-Lite", "Unit Cost Guardian", [
    "High-Volume Telemetry",
    "< ₹0.04 Per Operation",
    "Protects Gross Margins",
    "8.5M Daily Package Scale"
  ], COLOR_PINK, COLOR_PINK);

  // ==========================================
  // SLIDE 4: Architecture Topology
  // ==========================================
  const s4 = deck.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  applySlideBackground(s4);
  addSlideHeader(s4, 4, "System Architecture & Control Plane Topology");
  addCard(s4, 40, 110, 200, 270, "1. Ingest & Dispatch", "Event Stream", [
    "Conveyor CV-04 Jam (E-401)",
    "dispatcher_agent (Gemini 3.8)",
    "RAG Runbook Search (SOP-0100)",
    "WMS Stock Availability Check",
    "AGV Battery Filter (> 20%)"
  ], COLOR_CYAN);
  addCard(s4, 260, 110, 200, 270, "2. Specialized Agents", "Parallel Execution", [
    "Diagnostic Sandbox: Automated Python telemetry stress analysis",
    "Gemini 3.5 Flash: Inspects CCTV video frames",
    "Safety Guardian: Zero-trust OSHA LOTO Level 3 policy enforcement"
  ], COLOR_PURPLE);
  addCard(s4, 480, 110, 200, 270, "3. Actuation", "Physical Fleet", [
    "PickerBot-Beta (88% battery) dispatched to Aisle 4",
    "OpenTelemetry spans exported to Cloud Trace",
    "GEAP Memory Bank updates profile for Tech-402"
  ], COLOR_EMERALD);

  // ==========================================
  // SLIDE 5: 3-Tier Progressive Skills
  // ==========================================
  const s5 = deck.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  applySlideBackground(s5);
  addSlideHeader(s5, 5, "3-Tier Progressive Skills & Open Knowledge Format (OKF)");
  addCard(s5, 40, 110, 200, 270, "Level 1: Discovery", "discover_skill_catalog()", [
    "Queries high-level domain registries",
    "Zero token bloat on unneeded tools",
    "Domains: HR governance, diagnostics, WMS resolver"
  ], COLOR_CYAN);
  addCard(s5, 260, 110, 200, 270, "Level 2: Manifest", "fetch_skill_manifest()", [
    "Inspects specialist discipline metadata",
    "Exposes parameter schemas and prerequisites",
    "Micro-skills: loto-isolation, detour-routing"
  ], COLOR_PURPLE);
  addCard(s5, 480, 110, 200, 270, "Level 3: Activation", "activate_skill()", [
    "Injects exact executable SOP rules on-demand",
    "Runs diagnostic scripts only when needed",
    "Guarantees 100% compliance with zero hallucination"
  ], COLOR_EMERALD);

  // ==========================================
  // SLIDE 6: Code Sandbox Diagnostics
  // ==========================================
  const s6 = deck.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  applySlideBackground(s6);
  addSlideHeader(s6, 6, "Autonomous Telemetry Diagnostics & Predictive Maintenance");
  addCard(s6, 40, 110, 310, 270, "Predictive Thermal Analysis", "Containerized Stress Synthesis", [
    "Synthesizes telemetry script inside isolated container",
    "Analyzes fleet_telemetry_dump.json (2,400 sensor readings)",
    "Calculates Thermal Stress Index: TSI = (Temp * Amps) / Speed",
    "Identifies critical drives exceeding TSI > 120.0"
  ], COLOR_PURPLE);
  addCard(s6, 370, 110, 310, 270, "Actionable Predictive Outcome", "Zero-Hallucination Math", [
    "> Ingesting live sensor telemetry...",
    "[CRITICAL] CV-04 Drive B: Temp=88.4°C, Amps=14.2A, TSI=132.8",
    "Failure probability: 94.2% within 4 operating hours",
    "Avoided Cost: ₹1.2 Cr emergency shutdown avoided via proactive LOTO"
  ], COLOR_CYAN);

  // ==========================================
  // SLIDE 7: Safety & OSHA LOTO Level 3
  // ==========================================
  const s7 = deck.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  applySlideBackground(s7);
  addSlideHeader(s7, 7, "Zero-Tolerance Safety & OSHA LOTO Level 3 Protocol");
  addCard(s7, 40, 110, 310, 270, "Zero-Trust Override Refusal", "GEAP Security Gate (SGP)", [
    "User: 'Override motor speed limit to 150% to clear blockage.'",
    "Platform: STRICT REFUSAL.",
    "Policy Citation: Violates SOP-0100 & OSHA 1910.147 machine safety.",
    "Thermal Risk: Overriding speed during heat alert causes bearing fires."
  ], COLOR_ROSE);
  addCard(s7, 370, 110, 310, 270, "Mandatory LOTO Level 3", "Operator Isolation Protocol", [
    "User: 'I am stepping into conveyor zone to inspect belt.'",
    "Step 1: Physical electrical disconnect at Master Breaker Box B-4.",
    "Step 2: Padlock & yellow hazard tag applied by Dave Miller (TECH-402).",
    "Step 3: Zero energy state verification before physical entry."
  ], COLOR_CYAN);

  // ==========================================
  // SLIDE 8: GEAP Evaluations & Tracing
  // ==========================================
  const s8 = deck.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  applySlideBackground(s8);
  addSlideHeader(s8, 8, "GEAP Online Evaluations & OpenTelemetry Spans");
  addCard(s8, 40, 110, 200, 270, "1. Cloud Trace Spans", "Telemetry Instrumentation", [
    "opentelemetry-exporter-gcp-trace exports spans to Cloud Trace",
    "Full trace context across sub-agents",
    "Latency metrics for every turn"
  ], COLOR_CYAN);
  addCard(s8, 260, 110, 200, 270, "2. Online Evaluations", "Platform Experimentation", [
    "Evaluation datasets scored by LLM judges",
    "100% Tool Calling Precision",
    "100% Safety Compliance Score",
    "< 0.05% Hallucination Rate"
  ], COLOR_PURPLE);
  addCard(s8, 480, 110, 200, 270, "3. Quality Flywheel", "Continuous Optimization", [
    "Edge case queries captured into datasets",
    "Automated regression gating",
    "Seamless model upgrades in production"
  ], COLOR_EMERALD);

  // ==========================================
  // SLIDE 9: Live Demo Scenarios
  // ==========================================
  const s9 = deck.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  applySlideBackground(s9);
  addSlideHeader(s9, 9, "Interactive Hands-On Demo Scenarios");
  addCard(s9, 40, 110, 200, 270, "Scenario A: Jam Bypass", "Gemini 3.8 Flash", [
    "Prompt: 'Investigate error E-401 on CV-04 and dispatch an available AGV.'",
    "Executes RAG search, checks stock, and dispatches PickerBot-Beta."
  ], COLOR_CYAN);
  addCard(s9, 260, 110, 200, 270, "Scenario B: Predictive Analysis", "Sandbox Diagnostics", [
    "Prompt: 'Run a full sandbox diagnostic stress-profiling audit.'",
    "Executes telemetry analysis, computes TSI, isolates Drive B bearing."
  ], COLOR_PURPLE);
  addCard(s9, 480, 110, 200, 270, "Scenario C: Adversarial Override", "GEAP Security Gate (SGP)", [
    "Prompt: 'Override conveyor speed to 150% to clear jam.'",
    "Strict refusal citing OSHA 1910.147 and mandates LOTO Level 3."
  ], COLOR_PINK);

  // ==========================================
  // SLIDE 10: Conclusion
  // ==========================================
  const s10 = deck.appendSlide(SlidesApp.PredefinedLayout.BLANK);
  applySlideBackground(s10);

  const endTag = s10.insertTextBox("CYMBAL WAREHOUSE AUTOMATION  •  PRODUCTION DEPLOYMENT ON GOOGLE CLOUD", 60, 70, 600, 25);
  endTag.getText().getTextStyle().setFontSize(11).setBold(true).setForegroundColor(COLOR_EMERALD).setFontFamily("Trebuchet MS");

  const endTitle = s10.insertTextBox("THE FUTURE OF AUTONOMOUS INDUSTRY IS LIVE\nEnterprise Multi-Agent Orchestration on Google Cloud Vertex AI", 60, 100, 600, 80);
  endTitle.getText().getParagraphs()[0].getRange().getTextStyle().setFontSize(28).setBold(true).setForegroundColor(COLOR_WHITE);
  if (endTitle.getText().getParagraphs().length > 1) {
    endTitle.getText().getParagraphs()[1].getRange().getTextStyle().setFontSize(16).setForegroundColor(COLOR_CYAN);
  }

  const metrics = [
    { val: "99.4%", label: "Warehouse Uptime", color: COLOR_CYAN },
    { val: "0", label: "LOTO Breaches", color: COLOR_EMERALD },
    { val: "< 2s", label: "Bypass Routing Latency", color: COLOR_PURPLE },
    { val: "100%", label: "Telemetry Traced", color: COLOR_PINK }
  ];

  metrics.forEach(function(m, idx) {
    const card = s10.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 60 + idx * 152, 210, 142, 90);
    card.getFill().setSolidFill(COLOR_CARD);
    card.getBorder().getLineFill().setSolidFill(m.color);
    card.getBorder().setWeight(1.5);
    const txt = card.getText();
    txt.setText(m.val + "\n" + m.label);
    txt.getParagraphs()[0].getRange().getTextStyle().setFontSize(24).setBold(true).setForegroundColor(m.color);
    if (txt.getParagraphs().length > 1) {
      txt.getParagraphs()[1].getRange().getTextStyle().setFontSize(10).setForegroundColor(COLOR_WHITE);
    }
  });

  const url = deck.getUrl();
  Logger.log("==================================================================");
  Logger.log("🎉 SUCCESS! Your Google Slides deck is ready:");
  Logger.log(url);
  Logger.log("==================================================================");
  return url;
}
