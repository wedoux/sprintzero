const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  LevelFormat, PageNumber, PageBreak, TabStopType, TabStopPosition,
  Header, Footer
} = require('docx');
const fs = require('fs');

const BLUE_DARK  = "1B3A5C";
const BLUE_MID   = "2E6DA4";
const BLUE_LIGHT = "D6E8F7";
const GREY_LIGHT = "F5F7FA";
const GREY_TEXT  = "666666";
const AMBER      = "B07800";
const GREEN      = "276B47";
const WHITE      = "FFFFFF";

const b = (col="CCCCCC") => ({ style: BorderStyle.SINGLE, size: 1, color: col });
const borders = (col="CCCCCC") => ({ top:b(col), bottom:b(col), left:b(col), right:b(col) });
const noB = () => ({ style: BorderStyle.NONE, size: 0, color: "FFFFFF" });
const sp = (before=0, after=0) => ({ spacing: { before, after } });

function gap() { return new Paragraph({ ...sp(0,0), children:[] }); }

function rule(color=BLUE_MID) {
  return new Paragraph({
    ...sp(0,160),
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color, space: 1 } },
    children: []
  });
}

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    ...sp(320,80),
    children: [new TextRun({ text, font:"Arial", size:36, bold:true, color:BLUE_DARK })]
  });
}

function h2(text) {
  return [
    new Paragraph({
      heading: HeadingLevel.HEADING_2,
      ...sp(280,40),
      children: [new TextRun({ text, font:"Arial", size:26, bold:true, color:BLUE_MID })]
    }),
    rule(BLUE_MID)
  ];
}

function h3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    ...sp(200,60),
    children: [new TextRun({ text, font:"Arial", size:22, bold:true, color:BLUE_DARK })]
  });
}

function body(text, opts={}) {
  return new Paragraph({
    ...sp(0,120),
    children: [new TextRun({ text, font:"Arial", size:22, color:opts.color||"222222", bold:opts.bold||false, italics:opts.italic||false })]
  });
}

function callout(text, accent=AMBER) {
  return new Table({
    width: { size:9360, type:WidthType.DXA },
    columnWidths: [180, 9180],
    rows: [new TableRow({ children: [
      new TableCell({
        width:{size:180,type:WidthType.DXA}, borders:borders(accent),
        shading:{fill:accent,type:ShadingType.CLEAR},
        margins:{top:80,bottom:80,left:60,right:60},
        children:[new Paragraph({children:[]})]
      }),
      new TableCell({
        width:{size:9180,type:WidthType.DXA},
        borders:{top:b(accent),bottom:b(accent),left:{style:BorderStyle.NONE,size:0,color:"FFFFFF"},right:b(accent)},
        shading:{fill:GREY_LIGHT,type:ShadingType.CLEAR},
        margins:{top:100,bottom:100,left:160,right:160},
        children:[new Paragraph({...sp(0,0), children:[new TextRun({text, font:"Arial", size:20, color:"333333", italics:true})]})]
      })
    ]})]
  });
}

function headerRow(labels, widths) {
  return new TableRow({ tableHeader:true, children: labels.map((label,i) =>
    new TableCell({
      width:{size:widths[i],type:WidthType.DXA}, borders:borders(BLUE_DARK),
      shading:{fill:BLUE_DARK,type:ShadingType.CLEAR},
      margins:{top:80,bottom:80,left:120,right:120},
      children:[new Paragraph({...sp(0,0), children:[new TextRun({text:label,font:"Arial",size:20,bold:true,color:WHITE})]})]
    })
  )});
}

function dataRow(cells, widths, shade=false) {
  return new TableRow({ children: cells.map((cell,i) =>
    new TableCell({
      width:{size:widths[i],type:WidthType.DXA}, borders:borders("CCCCCC"),
      shading:{fill:shade?GREY_LIGHT:WHITE,type:ShadingType.CLEAR},
      margins:{top:60,bottom:60,left:120,right:120},
      children:[new Paragraph({...sp(0,0), children:[new TextRun({
        text:cell, font:"Arial", size:i===0?19:19,
        color:i===0?BLUE_DARK:"333333", bold:i===0
      })]})]
    })
  )});
}

function statusColor(s) {
  if (s==="EXISTS") return GREEN;
  if (s==="IN PROGRESS") return BLUE_MID;
  if (s==="PLANNED") return GREY_TEXT;
  if (s==="TEMPLATE") return AMBER;
  return GREY_TEXT;
}

// Registry entries
const entries = [
  // FOUNDATIONAL
  { id:"F-001", col:"Foundational", file:"ux_principles_and_heuristics.md",
    desc:"Core UX heuristics (Nielsen, Gestalt), cognitive load, mental models, affordances. The universal WHY behind design decisions.",
    topics:"usability, heuristics, cognitive load, mental models", domain:"general", strength:"canonical", status:"PLANNED" },
  { id:"F-002", col:"Foundational", file:"cognitive_biases_in_ux_research.md",
    desc:"Biases that distort research: confirmation bias, availability heuristic, framing effects, social desirability. How they corrupt data collection and synthesis.",
    topics:"bias, research quality, synthesis errors, framing", domain:"general", strength:"canonical", status:"PLANNED" },
  { id:"F-003", col:"Foundational", file:"research_methods_reference.md",
    desc:"Method-level knowledge: when to use interviews vs surveys vs diary studies vs App Store reviews. Signal-to-noise characteristics and generalisability limits of each.",
    topics:"interviews, surveys, diary studies, app store, NPS, generalisability", domain:"general", strength:"canonical", status:"PLANNED" },
  { id:"F-004", col:"Foundational", file:"ai_capabilities_and_constraints.md",
    desc:"What LLMs can and cannot do reliably in a research reasoning context. Confabulation mechanics, hallucination patterns, RAG vs generation distinction. SprintZero-specific constraints.",
    topics:"llm, hallucination, confabulation, rag, reliability", domain:"general", strength:"canonical", status:"PLANNED" },
  { id:"F-005", col:"Foundational", file:"insight_synthesis_failure_modes.md",
    desc:"Taxonomy of how UX insights go wrong: misclassification, overgeneralisation, theme conflation, underpowered evidence. The Weather Underground stale-data / forecast-accuracy case is the canonical worked example.",
    topics:"misclassification, synthesis, theme conflation, insight quality, failure modes", domain:"general", strength:"canonical", status:"EXISTS" },

  // APPLIED
  { id:"A-001", col:"Applied", file:"sprintzero_evaluation_framework.md",
    desc:"The core SprintZero evaluation protocol: STRONG / UNCERTAIN / WEAK verdicts, falsification test, transfer assumption check, decision-change vs decision-enable distinction. Reusable across corpora.",
    topics:"evaluation, verdicts, falsification, transfer assumption, protocol", domain:"general", strength:"canonical", status:"EXISTS" },
  { id:"A-002", col:"Applied", file:"corpus_annotation_protocol.md",
    desc:"How to annotate a corpus for SprintZero: review ID schema (R01–Rn), behavioural signal tagging, counter-signal identification, confidence scoring. Ensures corpora are consistent and citable.",
    topics:"annotation, corpus, review ids, signals, counter-signals, confidence", domain:"general", strength:"established", status:"PLANNED" },
  { id:"A-003", col:"Applied", file:"rag_registry_management.md",
    desc:"How to add, update, retire, and gap-flag corpora in the Registry. Versioning conventions, metadata schema, gap flag format. This document.",
    topics:"registry, metadata, versioning, gap flags, corpus management", domain:"general", strength:"established", status:"IN PROGRESS" },
  { id:"A-004", col:"Applied", file:"synthesis_prompt_templates.md",
    desc:"Structured system prompt templates for the composition layer. Covers: single-corpus evaluation, multi-corpus comparison, transfer assumption reasoning, gap-flagged response format.",
    topics:"prompts, synthesis, composition, system prompt, templates", domain:"general", strength:"established", status:"PLANNED" },
  { id:"A-005", col:"Applied", file:"benchmark_query_set.md",
    desc:"15 benchmark queries for evaluating retrieval quality. Includes expected retrieval characteristics, diversity requirements, and failure mode triggers. The evaluation instrument for each build phase.",
    topics:"evaluation, benchmarks, testing, retrieval quality, failure modes", domain:"general", strength:"established", status:"PLANNED" },

  // CONTEXTUAL
  { id:"C-001", col:"Contextual", file:"domain_weather_apps.md",
    desc:"Weather app UX domain knowledge: user trust formation, data freshness expectations, PWS density by geography, national meteorological alternatives (MeteoSwiss, DWD, Météo-France). Required for EU transfer assumption reasoning.",
    topics:"weather, trust, data freshness, PWS density, EU transfer, meteorological services", domain:"weather", strength:"established", status:"PLANNED" },
  { id:"C-002", col:"Contextual", file:"domain_fintech_compliance.md",
    desc:"Fintech UX constraints: regulatory onboarding requirements, KYC/AML friction patterns, user trust in financial data, EU vs US regulatory differences.",
    topics:"fintech, compliance, onboarding, KYC, AML, regulatory, trust", domain:"fintech", strength:"established", status:"PLANNED" },
  { id:"C-003", col:"Contextual", file:"domain_b2b_saas.md",
    desc:"B2B SaaS UX context: multi-stakeholder decision making, champion vs end-user vs buyer distinctions, enterprise onboarding complexity, admin/user permission dynamics.",
    topics:"b2b, saas, enterprise, stakeholders, onboarding, admin, permissions", domain:"b2b-saas", strength:"established", status:"PLANNED" },

  // SITUATIONAL
  { id:"S-001", col:"Situational", file:"corpus_weather_underground_app_store_reviews.md",
    desc:"13 annotated App Store reviews for Weather Underground (R01–R13). Dates, star ratings, behavioural signals, counter-signals flagged. The founding corpus. Demonstrates the stale-data / forecast-accuracy misclassification.",
    topics:"weather underground, app store, reviews, trust, stale data, forecast accuracy", domain:"weather", strength:"canonical", status:"EXISTS" },
  { id:"S-002", col:"Situational", file:"[project]_[source]_[date].md",
    desc:"Template slot for future project-specific corpora. Each new research project generates its own Situational file(s): transcripts by topic/speaker/phase, survey verbatims, NPS comments, support tickets.",
    topics:"project-specific, transcripts, surveys, NPS, support tickets", domain:"project", strength:"anecdotal", status:"TEMPLATE" },
];

function makeRegistryTable() {
  const widths = [680, 1100, 2320, 2580, 1180, 1500];
  const heads = ["ID","Collection","Filename","Description","Topics (sample)","Status"];

  const rows = entries.map((e,i) => new TableRow({ children: [
    new TableCell({ width:{size:widths[0],type:WidthType.DXA}, borders:borders("CCCCCC"),
      shading:{fill:i%2?GREY_LIGHT:WHITE,type:ShadingType.CLEAR}, margins:{top:60,bottom:60,left:120,right:120},
      children:[new Paragraph({...sp(0,0),children:[new TextRun({text:e.id,font:"Arial",size:18,bold:true,color:BLUE_DARK})]})] }),
    new TableCell({ width:{size:widths[1],type:WidthType.DXA}, borders:borders("CCCCCC"),
      shading:{fill:i%2?GREY_LIGHT:WHITE,type:ShadingType.CLEAR}, margins:{top:60,bottom:60,left:120,right:120},
      children:[new Paragraph({...sp(0,0),children:[new TextRun({text:e.col,font:"Arial",size:18,color:"333333"})]})] }),
    new TableCell({ width:{size:widths[2],type:WidthType.DXA}, borders:borders("CCCCCC"),
      shading:{fill:i%2?GREY_LIGHT:WHITE,type:ShadingType.CLEAR}, margins:{top:60,bottom:60,left:120,right:120},
      children:[new Paragraph({...sp(0,0),children:[new TextRun({text:e.file,font:"Courier New",size:17,color:BLUE_MID})]})] }),
    new TableCell({ width:{size:widths[3],type:WidthType.DXA}, borders:borders("CCCCCC"),
      shading:{fill:i%2?GREY_LIGHT:WHITE,type:ShadingType.CLEAR}, margins:{top:60,bottom:60,left:120,right:120},
      children:[new Paragraph({...sp(0,0),children:[new TextRun({text:e.desc,font:"Arial",size:17,color:"444444"})]})] }),
    new TableCell({ width:{size:widths[4],type:WidthType.DXA}, borders:borders("CCCCCC"),
      shading:{fill:i%2?GREY_LIGHT:WHITE,type:ShadingType.CLEAR}, margins:{top:60,bottom:60,left:120,right:120},
      children:[new Paragraph({...sp(0,0),children:[new TextRun({text:e.topics,font:"Arial",size:16,color:GREY_TEXT,italics:true})]})] }),
    new TableCell({ width:{size:widths[5],type:WidthType.DXA}, borders:borders("CCCCCC"),
      shading:{fill:statusColor(e.status),type:ShadingType.CLEAR}, margins:{top:60,bottom:60,left:80,right:80},
      children:[new Paragraph({alignment:AlignmentType.CENTER,...sp(0,0),children:[new TextRun({text:e.status,font:"Arial",size:16,bold:true,color:WHITE})]})] }),
  ]}));

  return new Table({ width:{size:9360,type:WidthType.DXA}, columnWidths:widths, rows:[headerRow(heads,widths),...rows] });
}

function makePipelineTable() {
  const widths = [1800,2100,5460];
  const rows = [
    ["Query Expansion","Lightweight LLM pre-pass","Enriches query surface for embedding. Not a classifier — enrichment only. If it fails, embeddings still work."],
    ["Parallel Retrieval","All collections simultaneously","No routing gates. All four collections queried in parallel. Top-k per collection returned independently."],
    ["Scoring + Boost","Embedding primary, metadata nudges","embedding_score + 0.10×topic_overlap + 0.10×domain_match + 0.05×strength_boost. Boosts nudge; they do not override."],
    ["Diversity Enforcement","Minimum coverage rules","≥1 Applied chunk if above threshold. ≥1 Contextual if domain detected. ≤2 chunks per source file."],
    ["Foundational Injection","Automatic fallback","If no Foundational chunk in top-N → inject highest-scoring F-series chunk. No hardcoding of which file."],
    ["Structured Synthesis","Composition prompt (reasoning contract)","WHY (Foundational) + HOW (Applied) + WHERE (Contextual) + THIS (Situational). Conflicts named and resolved explicitly."],
    ["Answer + Gap Flags","Always includes what is missing","Every answer states what corpus would improve confidence. Gap flags are never silent."],
  ];
  return new Table({ width:{size:9360,type:WidthType.DXA}, columnWidths:widths,
    rows:[headerRow(["Stage","Mechanism","Notes"],widths), ...rows.map((r,i)=>dataRow(r,widths,i%2===1))] });
}

function makeCollectionTable() {
  const widths = [1800,900,3000,3660];
  const rows = [
    ["Foundational","WHY","One concept, fully explained. Principles, cognitive biases, research fundamentals.","Vague, conceptual, explanatory queries"],
    ["Applied","HOW","One solution with context and rationale. Patterns, anti-patterns, flows, protocols.","Concrete, task-oriented queries"],
    ["Contextual","WHERE","One domain scenario, fully described. Constraints, regulations, user mental models.","Domain-specific, constraint queries"],
    ["Situational","THIS","Chunked by topic, speaker, or phase. Project transcripts, reviews, briefs, verbatims.","Evidence queries tied to a specific project"],
  ];
  return new Table({ width:{size:9360,type:WidthType.DXA}, columnWidths:widths,
    rows:[headerRow(["Collection","Role","Chunk Principle","Query Match Style"],widths), ...rows.map((r,i)=>dataRow(r,widths,i%2===1))] });
}

function makeMetadataTable() {
  const widths = [1400,3000,4960];
  const rows = [
    ["type","foundational | applied | contextual | situational","Collection role. Primary retrieval namespace signal."],
    ["topics",'["onboarding", "compliance", "trust"]',"Loose tags. Fuzzy matched against query expansion hints. Not an ontology — approximate is fine."],
    ["domain",'["fintech", "general"]',"Can be multi-valued. \"general\" means always eligible for retrieval regardless of domain detection."],
    ["strength","canonical | established | anecdotal","Canonical = foundational literature. Established = solid practice. Anecdotal = single-project data. Influences score boost."],
  ];
  return new Table({ width:{size:9360,type:WidthType.DXA}, columnWidths:widths,
    rows:[headerRow(["Field","Values","Purpose"],widths), ...rows.map((r,i)=>dataRow(r,widths,i%2===1))] });
}

function makeFailureTable() {
  const widths = [2000,2400,4960];
  const rows = [
    ["Domain not detected","Contextual chunks absent from retrieval","Answer proceeds on Foundational + Applied. Gap flag states what domain context would add."],
    ["Only patterns retrieve","No Foundational chunk in top-N","Foundational injection fires. Highest-scoring F-series chunk inserted automatically."],
    ["Project context contradicts principles","Situational conflicts with Foundational","Composition prompt requires conflict to be named and resolved explicitly. The contradiction becomes the answer."],
    ["Query too vague","Query expansion produces noise","Falls back to raw embedding on original query. Broad retrieval. Lower confidence signalled in output."],
    ["Missing corpus","No relevant Situational file exists","Answer proceeds on available knowledge. Gap flag: \"No [domain/project] corpus — answer based on general patterns only.\""],
    ["Metadata mismatch","Tags do not overlap with query hints","Embedding similarity carries full weight. Metadata boosts simply do not fire. System degrades gracefully."],
  ];
  return new Table({ width:{size:9360,type:WidthType.DXA}, columnWidths:widths,
    rows:[headerRow(["Failure Mode","Trigger","Designed Response"],widths), ...rows.map((r,i)=>dataRow(r,widths,i%2===1))] });
}

function makeBuildTable() {
  const widths = [900,2200,6260];
  const rows = [
    ["Phase 1","F-001, A-001, S-001","Raw embedding only. No metadata. No scoring boosts. Run 5 benchmark queries. Establish baseline. Add nothing until a failure justifies it."],
    ["Phase 2","F-002, F-003, C-001, A-002","Add metadata schema. Add topic overlap boost. Add first Contextual file (weather domain). Re-run benchmarks."],
    ["Phase 3","A-004, A-005","Add diversity enforcement. Add composition prompt. Add synthesis templates. Full 15-query benchmark run."],
    ["Phase 4","F-004, F-005, A-003, S-002+","Add Situational project corpora. Add gap flagging. Foundational injection live. Registry management file complete."],
    ["Phase 5","All remaining","Failure mode responses. Ambiguous query benchmarks. Additional Contextual domain files added as real projects demand them."],
  ];
  return new Table({ width:{size:9360,type:WidthType.DXA}, columnWidths:widths,
    rows:[headerRow(["Phase","Files Introduced","Focus"],widths), ...rows.map((r,i)=>dataRow(r,widths,i%2===1))] });
}

// ─── DOCUMENT ────────────────────────────────────────────────────────────────

const doc = new Document({
  styles: {
    default: { document: { run: { font:"Arial", size:22 } } },
    paragraphStyles: [
      { id:"Heading1", name:"Heading 1", basedOn:"Normal", next:"Normal", quickFormat:true,
        run:{size:36,bold:true,font:"Arial",color:BLUE_DARK}, paragraph:{spacing:{before:320,after:80},outlineLevel:0} },
      { id:"Heading2", name:"Heading 2", basedOn:"Normal", next:"Normal", quickFormat:true,
        run:{size:26,bold:true,font:"Arial",color:BLUE_MID}, paragraph:{spacing:{before:280,after:40},outlineLevel:1} },
      { id:"Heading3", name:"Heading 3", basedOn:"Normal", next:"Normal", quickFormat:true,
        run:{size:22,bold:true,font:"Arial",color:BLUE_DARK}, paragraph:{spacing:{before:200,after:60},outlineLevel:2} },
    ]
  },
  numbering: {
    config: [
      { reference:"bullets", levels:[{level:0,format:LevelFormat.BULLET,text:"•",alignment:AlignmentType.LEFT,
        style:{paragraph:{indent:{left:720,hanging:360}}}}] }
    ]
  },
  sections: [{
    properties: {
      page: { size:{width:12240,height:15840}, margin:{top:1440,right:1440,bottom:1440,left:1440} }
    },
    headers: {
      default: new Header({ children: [
        new Paragraph({
          ...sp(0,0),
          border:{bottom:{style:BorderStyle.SINGLE,size:4,color:BLUE_DARK,space:1}},
          children:[
            new TextRun({text:"SprintZero  ·  RAG Registry V1",font:"Arial",size:18,color:BLUE_MID}),
            new TextRun({text:"    Niko  ·  May 2026",font:"Arial",size:18,color:GREY_TEXT}),
          ]
        })
      ]})
    },
    footers: {
      default: new Footer({ children: [
        new Paragraph({
          ...sp(0,0),
          border:{top:{style:BorderStyle.SINGLE,size:4,color:"CCCCCC",space:1}},
          tabStops:[{type:TabStopType.RIGHT,position:TabStopPosition.MAX}],
          children:[
            new TextRun({text:"SprintZero is a reasoning QA layer — not a research tool",font:"Arial",size:16,color:GREY_TEXT,italics:true}),
            new TextRun({text:"\t",font:"Arial",size:16}),
            new TextRun({children:[PageNumber.CURRENT],font:"Arial",size:16,color:GREY_TEXT}),
          ]
        })
      ]})
    },
    children: [
      // COVER
      new Paragraph({...sp(480,0), children:[new TextRun({text:"SprintZero",font:"Arial",size:64,bold:true,color:BLUE_DARK})]}),
      new Paragraph({...sp(0,80), children:[new TextRun({text:"RAG Registry",font:"Arial",size:48,color:BLUE_MID})]}),
      new Paragraph({...sp(0,60), children:[new TextRun({text:"Version 1  ·  May 2026",font:"Arial",size:24,color:GREY_TEXT})]}),
      rule(BLUE_DARK),
      gap(),
      new Paragraph({...sp(0,100), children:[new TextRun({text:"The index of all knowledge available to the SprintZero reasoning system. It specifies what exists, what is planned, what is missing, and how each file should be retrieved.",font:"Arial",size:22,color:"333333",italics:true})]}),
      new Paragraph({...sp(0,0), children:[new TextRun({text:"This is a living document. Every time a new corpus or framework file is created, it is registered here first.",font:"Arial",size:22,color:GREY_TEXT})]}),
      gap(),

      // 1. PURPOSE
      new Paragraph({children:[new PageBreak()]}),
      h1("1.  Purpose"),
      rule(BLUE_DARK),
      gap(),
      body("SprintZero is an AI-augmented research reasoning system. Its core job is not to generate insights — it is to evaluate them. It catches the quiet failure mode that kills most UX research programmes: good data, poorly reasoned into wrong conclusions, invested in confidently."),
      gap(),
      body("The RAG Registry is the directory layer that makes this possible at scale. It sits above the individual RAG files and answers three questions the system must answer before it can reason well:"),
      gap(),
      ...["What knowledge does the system currently have access to?",
          "What knowledge is missing — and what corpus would need to exist to fill the gap?",
          "How should a given piece of knowledge be weighted in retrieval?"].map(t =>
        new Paragraph({numbering:{reference:"bullets",level:0},...sp(0,80),children:[new TextRun({text:t,font:"Arial",size:22,color:"333333"})]})),
      gap(),
      callout("The Registry transforms SprintZero from a tool into infrastructure. A single corpus limits the system to pattern-matching within one dataset. The Registry turns SprintZero into a research memory — an institutional record of what has been studied, what has been validated, and where the gaps are.", BLUE_MID),
      gap(),

      // 2. GOVERNING PRINCIPLE
      ...h2("2.  Governing Principle"),
      gap(),
      new Paragraph({...sp(80,160), alignment:AlignmentType.CENTER, children:[new TextRun({text:"Embeddings do the work.  Structure makes it inspectable.  Evaluation makes it improvable.",font:"Arial",size:26,bold:true,color:BLUE_DARK,italics:true})]}),
      gap(),
      body("Nothing in this architecture requires the system to be smart about routing. Every component degrades gracefully. If metadata matching fails, embedding similarity carries the answer. If domain detection fails, the answer proceeds on Foundational and Applied knowledge and flags the gap. A system that only works when everything is classified correctly will fail constantly."),
      gap(),

      // 3. ARCHITECTURE
      ...h2("3.  Architecture — Four Knowledge Collections"),
      gap(),
      body("SprintZero uses four knowledge collections, not tiers. The distinction matters: tiers imply routing gates. Collections are namespaces that embeddings retrieve across in parallel. No gate decides which collection a query reaches."),
      gap(),
      makeCollectionTable(),
      gap(),

      // 4. RETRIEVAL PIPELINE
      new Paragraph({children:[new PageBreak()]}),
      ...h2("4.  Retrieval Pipeline"),
      gap(),
      makePipelineTable(),
      gap(),
      gap(),
      h3("Metadata Schema"),
      body("Each file carries lightweight metadata. It supports retrieval — it does not drive it. If metadata is absent or mismatched, embeddings still work."),
      gap(),
      makeMetadataTable(),
      gap(),
      gap(),
      h3("Scoring Function"),
      new Paragraph({...sp(80,120), children:[new TextRun({text:"final_score  =  embedding_score  +  0.10 × topic_overlap  +  0.10 × domain_match  +  0.05 × strength_boost",font:"Courier New",size:20,color:BLUE_DARK})]}),
      body("Boosts are small by design. They nudge; they do not override. A highly relevant anecdotal chunk beats a weakly relevant canonical one."),
      gap(),

      // 5. FAILURE MODES
      ...h2("5.  Designed Failure Modes"),
      gap(),
      body("These are not edge cases. They are the most common scenarios in real research use. Each has a designed response rather than a silent failure."),
      gap(),
      makeFailureTable(),
      gap(),

      // 6. REGISTRY
      new Paragraph({children:[new PageBreak()]}),
      ...h2("6.  RAG Registry — Full File Index"),
      gap(),
      body("Every file that enters the SprintZero system must be registered here before use. Status is updated as files are created. The Registry is the source of truth for what the system knows."),
      gap(),
      // Legend
      (() => {
        const lw = [1200,1200,1200,1200,1200,3360];
        return new Table({ width:{size:9360,type:WidthType.DXA}, columnWidths:lw, rows:[
          new TableRow({ children:[
            new TableCell({width:{size:lw[0],type:WidthType.DXA},borders:borders(GREEN),shading:{fill:GREEN,type:ShadingType.CLEAR},margins:{top:60,bottom:60,left:120,right:120},children:[new Paragraph({...sp(0,0),children:[new TextRun({text:"EXISTS",font:"Arial",size:18,bold:true,color:WHITE})]})]}),
            new TableCell({width:{size:lw[1],type:WidthType.DXA},borders:borders(BLUE_MID),shading:{fill:BLUE_MID,type:ShadingType.CLEAR},margins:{top:60,bottom:60,left:120,right:120},children:[new Paragraph({...sp(0,0),children:[new TextRun({text:"IN PROGRESS",font:"Arial",size:17,bold:true,color:WHITE})]})]}),
            new TableCell({width:{size:lw[2],type:WidthType.DXA},borders:borders(GREY_TEXT),shading:{fill:GREY_TEXT,type:ShadingType.CLEAR},margins:{top:60,bottom:60,left:120,right:120},children:[new Paragraph({...sp(0,0),children:[new TextRun({text:"PLANNED",font:"Arial",size:18,bold:true,color:WHITE})]})]}),
            new TableCell({width:{size:lw[3],type:WidthType.DXA},borders:borders(AMBER),shading:{fill:AMBER,type:ShadingType.CLEAR},margins:{top:60,bottom:60,left:120,right:120},children:[new Paragraph({...sp(0,0),children:[new TextRun({text:"TEMPLATE",font:"Arial",size:17,bold:true,color:WHITE})]})]}),
            new TableCell({width:{size:lw[4]+lw[5],type:WidthType.DXA},borders:borders("CCCCCC"),shading:{fill:GREY_LIGHT,type:ShadingType.CLEAR},margins:{top:60,bottom:60,left:120,right:120},
              columnSpan:2,
              children:[new Paragraph({...sp(0,0),children:[new TextRun({text:"File created and in use  ·  Actively being built  ·  Defined, not yet created  ·  Slot for future files",font:"Arial",size:17,color:GREY_TEXT,italics:true})]})]}),
          ]})
        ]});
      })(),
      gap(),
      makeRegistryTable(),
      gap(),

      // 7. BUILD SEQUENCE
      new Paragraph({children:[new PageBreak()]}),
      ...h2("7.  Build Sequence"),
      gap(),
      body("Complexity is added only when a specific benchmark failure justifies it. Each phase has a clear before/after. When something breaks, the pipeline stage is identifiable."),
      gap(),
      makeBuildTable(),
      gap(),
      gap(),
      callout("Phase 1 is the only phase that matters right now. Two files. Five queries. A baseline. Everything else is the north star.", BLUE_MID),
      gap(),

      // 8. GOVERNANCE
      ...h2("8.  Registry Governance"),
      gap(),
      body("Rules for keeping the Registry honest as the system grows:"),
      gap(),
      ...["Every file must be registered before it enters the system. No unregistered files in production.",
          "Status must be kept current. A file marked PLANNED that has been created without updating the Registry is a gap.",
          "Gap flags in system output must be traceable to a missing Registry entry. If a gap flag appears for a corpus that should exist, the Registry has failed.",
          "Strength ratings are assigned at creation and reviewed when a file is updated. Anecdotal files may be promoted to established if validated across multiple projects.",
          "Situational files are project-scoped. They are retired (not deleted) when a project closes. The Registry retains the entry with status ARCHIVED and a closing date.",
      ].map(t => new Paragraph({numbering:{reference:"bullets",level:0},...sp(0,100),children:[new TextRun({text:t,font:"Arial",size:22,color:"333333"})]})),
      gap(),
      gap(),

      // CLOSE
      rule(BLUE_DARK),
      gap(),
      new Paragraph({...sp(0,0), alignment:AlignmentType.CENTER, children:[new TextRun({text:"SprintZero  ·  RAG Registry V1  ·  Niko  ·  May 2026",font:"Arial",size:18,color:GREY_TEXT,italics:true})]}),
    ]
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("/home/claude/SprintZero_RAG_Registry_V1.docx", buf);
  console.log("Done.");
});
