#!/usr/bin/env python3
"""Generate IT 6903 past-paper model answers PDF from lecture notes + revision notes."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    KeepTogether,
    HRFlowable,
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

OUT = "/workspace/IT6903-Scientific-Communication-Past-Paper-Answers.pdf"

NAVY = HexColor("#1a365d")
TEAL = HexColor("#2c5282")
LIGHT = HexColor("#edf2f7")
ACCENT = HexColor("#2b6cb0")


def styles():
    base = getSampleStyleSheet()
    s = {
        "title": ParagraphStyle(
            "TitleMain",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=16,
            textColor=NAVY,
            spaceAfter=6,
            alignment=TA_CENTER,
            leading=20,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10,
            textColor=TEAL,
            spaceAfter=4,
            alignment=TA_CENTER,
            leading=13,
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            textColor=HexColor("#4a5568"),
            spaceAfter=10,
            alignment=TA_CENTER,
            leading=12,
        ),
        "qhead": ParagraphStyle(
            "QHead",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=13,
            textColor=white,
            spaceBefore=0,
            spaceAfter=0,
            leading=16,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11,
            textColor=NAVY,
            spaceBefore=10,
            spaceAfter=4,
            leading=14,
        ),
        "part": ParagraphStyle(
            "Part",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=10,
            textColor=ACCENT,
            spaceBefore=8,
            spaceAfter=3,
            leading=13,
        ),
        "body": ParagraphStyle(
            "BodyJust",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            textColor=black,
            alignment=TA_JUSTIFY,
            spaceAfter=4,
            leading=13,
        ),
        "bullet": ParagraphStyle(
            "BulletJust",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            textColor=black,
            leftIndent=12,
            spaceAfter=2,
            leading=12.5,
        ),
        "mark": ParagraphStyle(
            "Mark",
            parent=base["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=8.5,
            textColor=HexColor("#718096"),
            spaceAfter=4,
            leading=11,
        ),
        "tf": ParagraphStyle(
            "TF",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.5,
            textColor=NAVY,
            spaceBefore=4,
            spaceAfter=2,
            leading=12,
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            textColor=HexColor("#718096"),
            alignment=TA_CENTER,
        ),
    }
    return s


def q_banner(text, s):
    data = [[Paragraph(text, s["qhead"])]]
    t = Table(data, colWidths=[16.5 * cm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return t


def build():
    s = styles()
    doc = SimpleDocTemplate(
        OUT,
        pagesize=A4,
        leftMargin=1.6 * cm,
        rightMargin=1.6 * cm,
        topMargin=1.4 * cm,
        bottomMargin=1.6 * cm,
        title="IT 6903 Past Paper Answers – Scientific Communication",
        author="Revision guide (lecture notes + handwritten notes)",
    )
    story = []

    story.append(Paragraph("IT 6903 – Scientific Communication", s["title"]))
    story.append(
        Paragraph(
            "Complete Model Answers · Batch 17 Past Paper (February 2026)",
            s["subtitle"],
        )
    )
    story.append(
        Paragraph(
            "University of Moratuwa · M.Sc / PG Diploma in Artificial Intelligence<br/>"
            "Prepared from Prof. Asoka S. Karunananda lecture notes (IT 5913) "
            "and student revision notes",
            s["meta"],
        )
    )
    story.append(HRFlowable(width="100%", thickness=1, color=NAVY, spaceAfter=10))

    # ========== Q1 ==========
    story.append(q_banner("Question 1 — Communication, Language &amp; AI  [25 marks]", s))

    story.append(Paragraph("(a) Human communication and AI  [3 × 3 = 9 marks]", s["section"]))

    story.append(Paragraph("(i) Distinctive feature of human communication", s["part"]))
    story.append(
        Paragraph(
            "<b>Answer:</b> The distinctive feature is <b>symbolic language</b> — "
            "the ability to use symbols such as words, letters, and numbers to "
            "manipulate and communicate meaning.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "Unlike animal communication (signals, calls, body language), humans "
            "can invent and share <b>stories</b> and knowledge that are preserved "
            "across generations. Through symbolic language we can collect, store, "
            "transmit, and discover new knowledge. Lecture emphasis: humanity became "
            "so capable over other animals largely due to this communication ability "
            "(storytelling for the next generation). Symbolic manipulation of language "
            "also underpins mathematics, science, engineering, and computing.",
            s["body"],
        )
    )

    story.append(Paragraph("(ii) Technologies for man–man, man–machine, machine–machine", s["part"]))
    story.append(
        Paragraph(
            "<b>(p) Man–man:</b> telephone, email, video conferencing, written documents "
            "(papers/thesis), messaging apps.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "<b>(q) Man–machine:</b> chatbots / LLMs (e.g. ChatGPT), computers, "
            "smartphones, expert systems, brain–computer interfaces (BCI), EEG-based systems.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "<b>(r) Machine–machine:</b> ATM ↔ bank servers, APIs between services, "
            "Multi-Agent Systems (MAS), IoT device-to-device protocols. "
            "Lecture note: machine-to-machine communication is now possible without humans.",
            s["bullet"],
        )
    )

    story.append(Paragraph("(iii) “AI is approaching the technological singularity in language processing.”", s["part"]))
    story.append(
        Paragraph(
            "<b>Position:</b> Agree <b>partially</b>, with strong caveats.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "Modern LLMs (e.g. ChatGPT) show impressive language processing and can "
            "appear near-human in many tasks. However, singularity (machine intelligence "
            "surpassing and escaping human control in a transformative way) is <b>not yet "
            "reached</b> in language AI because of major limitations:",
            s["body"],
        )
    )
    story.append(Paragraph("- <b>Hallucination</b> — models invent plausible but false content.", s["bullet"]))
    story.append(
        Paragraph(
            "- <b>Explainability</b> — non-symbolic ML is hard to interpret; lecture "
            "stresses synergy with symbolic AI / neuro-symbolic approaches.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "- Lack of reliable pragmatics, grounded understanding, and guaranteed truthfulness.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "So AI is advancing fast in language processing, but claiming singularity "
            "is overstated until these gaps are closed.",
            s["body"],
        )
    )

    story.append(Paragraph("(b) True / False with justification  [4 × 3 = 12 marks]", s["section"]))

    story.append(Paragraph("(i) Biological programming enables communication between plants and/or animals.", s["part"]))
    story.append(
        Paragraph(
            "<b>TRUE.</b> After Turing, people programmed computers; nowadays people "
            "also program plants and animals via <b>biological programming / biological "
            "computing</b>. Lecture: we are heading towards communication with plants "
            "and animals through biological computing — changing biological systems "
            "(including genetic-level programming) so they can be instructed/controlled "
            "in a communication-like way.",
            s["body"],
        )
    )

    story.append(
        Paragraph(
            "(ii) There is a synergy between recent developments in non-symbolic AI and "
            "symbolic AI in language processing.",
            s["part"],
        )
    )
    story.append(
        Paragraph(
            "<b>TRUE.</b> Non-symbolic AI (ML/LLMs/Transformers) is strong at "
            "generating language and learning from data, but weak at explainability. "
            "Symbolic AI (rules, logic, expert systems) provides explainability and "
            "structured reasoning. Lecture examples include addressing explainability "
            "in ML with symbolic AI / Expert Systems, and neuro-symbolic AI — combining "
            "both for better language systems.",
            s["body"],
        )
    )

    story.append(
        Paragraph(
            "(iii) Before the birth of AI, Alan Turing emphasized the role of "
            "communication in determining machine intelligence.",
            s["part"],
        )
    )
    story.append(
        Paragraph(
            "<b>TRUE.</b> The Turing Test judges intelligence by whether a machine "
            "can communicate so well that it fools a human into thinking it is human. "
            "Thus Turing placed communication at the centre of defining machine intelligence, "
            "before AI became an established field.",
            s["body"],
        )
    )

    story.append(Paragraph("(iv) Syntax is the most critical concern when communicating algorithmically.", s["part"]))
    story.append(
        Paragraph(
            "<b>FALSE.</b> A language has four major aspects — <b>lexicon, syntax, "
            "semantics, and pragmatics</b> — and <b>all four</b> must be developed. "
            "Coding shows this: wrong words (lexicon), wrong grammar (syntax), wrong "
            "meaning (semantics), or wrong order/flow (pragmatics) all break communication. "
            "Syntax alone is not the most critical concern.",
            s["body"],
        )
    )

    story.append(Paragraph("(c) Cognitive features  [4 marks]", s["section"]))
    story.append(Paragraph("(i) One education-related cognitive feature that enhances other abilities", s["part"]))
    story.append(
        Paragraph(
            "<b>Thinking</b> (algorithmic / language-related thinking). "
            "Lecture: reading activates/wakes up thinking, leading to understanding; "
            "thinking supports memory formation (neural circuits). Improving thinking "
            "(via math, programming, AI exercises, games, puzzles) enhances related "
            "cognitive skills such as understanding, memory, and communication.",
            s["body"],
        )
    )
    story.append(Paragraph("(ii) AI-based solution + one negative implication", s["part"]))
    story.append(
        Paragraph(
            "<b>Solution:</b> An AI-based interactive educational game (or AI agent for "
            "attention/mindfulness training) that trains thinking through puzzles, "
            "problem-solving, and guided reflection.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>Negative implication:</b> gaming / technology addiction — overuse may "
            "reduce real-world learning, attention, or social engagement. "
            "(Lecture principle: technology should make life easier, but if removed we "
            "should not be paralyzed.)",
            s["body"],
        )
    )

    story.append(PageBreak())

    # ========== Q2 ==========
    story.append(q_banner("Question 2 — Reading &amp; Research Literacy  [25 marks]", s))

    story.append(Paragraph("(a) Reading research papers  [3 × 3 = 9 marks]", s["section"]))

    story.append(Paragraph("(i) Two broad categories of information + what a novice gains", s["part"]))
    story.append(
        Paragraph(
            "<b>Two broad categories</b> extracted from research papers "
            "(lecture framing of scientific documents):",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "1. <b>Problem-related information</b> — background, gap, issues, "
            "failures/successes of others, importance of the problem.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "2. <b>Solution-related information</b> — technologies, methods, approaches, "
            "design/implementation ideas, evaluations.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "<b>Additional gains for a novice:</b> map of major universities/people/"
            "institutes/journals/conferences in the area; improved writing style and "
            "vocabulary; how arguments and citations are structured; references leading "
            "to further papers.",
            s["body"],
        )
    )

    story.append(
        Paragraph(
            "(ii) Three negative implications of AI-summarize → write proposal; analogy; correct use",
            s["part"],
        )
    )
    story.append(Paragraph("<b>Three immediate negative implications:</b>", s["body"]))
    story.append(
        Paragraph(
            "1. <b>Weak reading comprehension</b> — the student never deeply processes the papers.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "2. <b>Weak analytical thinking</b> — cannot judge gaps, +/− of technologies, or define an original problem.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "3. <b>Poor note-taking / ownership of knowledge</b> — no personal summaries; "
            "vocabulary and writing skill stagnate; risk of unread or hallucinated content "
            "entering the proposal.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "<b>Analogy:</b> Always using GPS without learning the map — when the tool fails "
            "(or invents a wrong route), you are lost. Lecture: if you know how to write/read, "
            "technology improves you; otherwise technology kills your ability.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>Correct use:</b> (1) Human reads and does the cognitive task first "
            "(summaries in own words, notes, problem/technology extraction); "
            "(2) then ask the machine to improve language/structure — not to replace thinking.",
            s["body"],
        )
    )

    story.append(Paragraph("(iii) Techniques that improve reading comprehension", s["part"]))
    story.append(
        Paragraph(
            "<b>(i) Reading aloud:</b> doubles perceptual input (eyes + ears). "
            "Strengthens thinking and memory; lecture: reading a little loudly improves understanding.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>(ii) Reading highlighted text:</b> underlining/highlighting focuses attention "
            "on problem/technology concepts, supports remembrance and understanding, "
            "and guides later detailed reading of the body.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>(iii) Automating left-to-right eye movement:</b> the brain splits tasks — "
            "eye movement (right-brain skill) vs understanding (left-brain). If L→R scanning "
            "becomes automatic through practice, energy is freed for understanding rather "
            "than hunting words. Use a pen/ruler and avoid focusing beyond the current line.",
            s["body"],
        )
    )

    story.append(Paragraph("(b) True / False with justification  [4 × 3 = 12 marks]", s["section"]))

    story.append(Paragraph("(i) In double-blind review, reviewers send comments directly to authors.", s["part"]))
    story.append(
        Paragraph(
            "<b>FALSE.</b> In the publication process, authors submit to the <b>editor</b>; "
            "reviewers assess quality and send comments to the editor; the editor decides "
            "and communicates with authors. Reviewers do not independently send comments "
            "directly to authors (especially in double-blind, identities are hidden).",
            s["body"],
        )
    )

    story.append(
        Paragraph(
            "(ii) Researcher credibility is assessed using multiple metrics derived from two main parameters.",
            s["part"],
        )
    )
    story.append(
        Paragraph(
            "<b>TRUE.</b> Credibility is commonly assessed via metrics built from "
            "<b>publications</b> and <b>citations</b> (and related indexes / impact factors). "
            "Examples: citation indexes (Scopus, Google Scholar, Web of Science), "
            "impact factor of journals, h-index-style measures derived from those bases.",
            s["body"],
        )
    )

    story.append(
        Paragraph(
            "(iii) Since knowledge is power, a bigger portion of finances in publishing goes to authors.",
            s["part"],
        )
    )
    story.append(
        Paragraph(
            "<b>FALSE.</b> Although authors create knowledge, the larger share of "
            "publishing income typically goes to <b>publishers</b> (and related commercial "
            "structures). Author royalties are comparatively small (lecture mentions "
            "royalty around ~10% in the publishing storyboard). Knowledge is power, but "
            "financial control of publication often sits with publishers/indexes.",
            s["body"],
        )
    )

    story.append(Paragraph("(iv) Reading and writing are activities that naturally demand mindfulness.", s["part"]))
    story.append(
        Paragraph(
            "<b>TRUE.</b> Many tasks (walking, eating, listening to music) can be done "
            "together; reading and writing generally cannot — they require attention on "
            "one thing so neural circuits can form. If a task is fully trained/automatic, "
            "mindfulness ≈ 0; reading/writing remain mindfulness-demanding cognitive work.",
            s["body"],
        )
    )

    story.append(Paragraph("(c) Best practices in reading for a research project  [4 marks]", s["section"]))
    story.append(Paragraph("(i) Best practices", s["part"]))
    story.append(
        Paragraph(
            "- Read <b>Abstract → Introduction → Conclusion</b> first to identify problem "
            "and technology concepts.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "- Highlight/underline important points; then read body for details of marked concepts.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "- Write <b>summaries/notes in your own words</b> (problem, technology, +/−).",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "- Use a <b>reference manager</b> (e.g. Zotero) for download, tags, notes, related papers.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "- Start from a review paper; follow its reference chain; organize reading around gap + technology.",
            s["bullet"],
        )
    )

    story.append(Paragraph("(ii) Most influential practice energizing ≥3 cognitive skills", s["part"]))
    story.append(
        Paragraph(
            "<b>Note-taking / writing summaries in your own words</b> is the most influential. "
            "A note acts as a <b>cognitive device</b>. It energizes at least:",
            s["body"],
        )
    )
    story.append(Paragraph("1. <b>Thinking</b> — selecting and restructuring ideas;", s["bullet"]))
    story.append(Paragraph("2. <b>Understanding</b> — restating meaning forces comprehension;", s["bullet"]))
    story.append(
        Paragraph(
            "3. <b>Memory</b> — writing helps remember what was read "
            "(lecture: writing helps remember what you wrote).",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "It also improves vocabulary and later writing of proposal/thesis chapters "
            "(Literature Review is a collection of such summaries).",
            s["body"],
        )
    )

    story.append(PageBreak())

    # ========== Q3 ==========
    story.append(q_banner("Question 3 — Scientific Documents &amp; Thesis Writing  [25 marks]", s))

    story.append(Paragraph("(a) Scientific documents in the research process  [3 × 3 = 9 marks]", s["section"]))

    story.append(Paragraph("(i) Four major scientific documents; content of the first; two topics", s["part"]))
    story.append(
        Paragraph(
            "<b>Four major documents:</b> (1) <b>Research / Project Proposal</b>, "
            "(2) <b>Progress Report</b>, (3) <b>Conference Paper</b>, (4) <b>Thesis</b> "
            "(journal paper is a related later form for wider access).",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "Any scientific document talks about two main topics: <b>Problem</b> and "
            "<b>Solution</b> (course title framing: Problem + Solution).",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>First document = Project Proposal (Ability Report).</b> Typical content:",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "Title (problem + technology), Introduction (gap + proposed solution), "
            "Objectives (problem-related + solution-related), Literature Review "
            "(others’ work → problem/technology), Problem in Brief, Proposed Solution/"
            "Approach (hypothesis, input, output, process, features, users), Resources, "
            "Plan of Action, References.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>Distribution of the two topics:</b> Problem-heavy early (intro background, "
            "LR, problem definition); Solution-heavy later (approach/design note). "
            "Abstract often balances problem–solution–outcome.",
            s["body"],
        )
    )

    story.append(Paragraph("(ii) Most influential chapter for developing the entire thesis", s["part"]))
    story.append(
        Paragraph(
            "<b>Literature Review.</b> It is the turning point where you know the "
            "<b>problem/gap</b> and the <b>technology/inspiration</b>. From LR you can "
            "derive title, hypothesis, objectives, approach, and the direction of all "
            "later chapters (technology, design, implementation, evaluation). "
            "Without a strong LR, the thesis has no justified problem or method.",
            s["body"],
        )
    )

    story.append(Paragraph("(iii) Stage to conceptualize the entire project; content to develop", s["part"]))
    story.append(
        Paragraph(
            "<b>Stage:</b> after adequate reviewing, at the <b>Project Proposal</b> stage "
            "(when Approach can be conceptualized).",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>Content:</b> hypothesis; input/output/process (technology); users; "
            "features; objectives; problem in brief; proposed solution; resources; "
            "plan of action mapped to objectives. Approach is the key step in the "
            "research process.",
            s["body"],
        )
    )

    story.append(Paragraph("(b) True / False with justification  [4 × 3 = 12 marks]", s["section"]))

    story.append(Paragraph("(i) Thesis chapters must be carefully developed in sequential chapter order.", s["part"]))
    story.append(
        Paragraph(
            "<b>FALSE.</b> Writing is <b>incremental</b>, not strictly sequential. "
            "Practically, develop Literature Review and then Approach early; later "
            "expand Design, Implementation, Evaluation. Outline → draft → revise → "
            "fine-tune is bidirectional. You cannot write a thesis in one shot in "
            "strict chapter order from page 1.",
            s["body"],
        )
    )

    story.append(
        Paragraph(
            "(ii) In the Milestone Approach, “Methodology” is adapted to suit steps in computing projects.",
            s["part"],
        )
    )
    story.append(
        Paragraph(
            "<b>TRUE.</b> In computing/AI projects, the general term Methodology is "
            "operationalized as milestone stages such as Technology → Approach → Design → "
            "Implementation → Evaluation (rather than a vague single “methods” chapter). "
            "This suits software/AI research workflows and maps to proposal → progress → "
            "conference paper → thesis milestones.",
            s["body"],
        )
    )

    story.append(
        Paragraph(
            "(iii) For good reasons, both objectives and problem definition should come before the Literature Review.",
            s["part"],
        )
    )
    story.append(
        Paragraph(
            "<b>FALSE.</b> <b>Objectives</b> can appear early (proposal/intro structure), "
            "but <b>problem definition</b> should come <b>after</b> the Literature Review. "
            "The researcher must know the literature to define the gap properly. "
            "Putting problem definition before LR loses justification and confuses the reader.",
            s["body"],
        )
    )

    story.append(
        Paragraph(
            "(iv) Only a few Research Software offer facilities to develop all sections/chapters as per a research method.",
            s["part"],
        )
    )
    story.append(
        Paragraph(
            "<b>TRUE.</b> Few platforms support the full research-document lifecycle "
            "aligned to a method. Lecture points students to specialized support such as "
            "<b>InPRAWeb</b> (https://inpraweb.lib.uom.lk/) for developing research writing "
            "across sections/chapters — not general office tools alone.",
            s["body"],
        )
    )

    story.append(Paragraph("(c) Outline–Draft–Revise–Fine-tune framework  [4 marks]", s["section"]))
    story.append(Paragraph("(i) People involved in the four stages", s["part"]))
    story.append(
        Paragraph(
            "- <b>Outline:</b> Student + Supervisor (agree structure/headings).",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "- <b>Draft:</b> mainly Student (write under headings; remove blank-page fear).",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "- <b>Revise:</b> Student (many times) + Supervisor (about 1–2 times) to improve content/flow.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "- <b>Fine-tune:</b> language improvement — Student and/or language editor; "
            "supervisor may guide academic tone.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "Justification: supervisor shapes research direction at outline/revise; "
            "student owns drafting; language polishing should not replace the student’s "
            "thinking.",
            s["body"],
        )
    )

    story.append(Paragraph("(ii) Using AI without harming language skills", s["part"]))
    story.append(
        Paragraph(
            "Use AI <b>after</b> you have outlined and drafted in your own words. "
            "Ask AI to improve clarity, grammar, or structure of <b>your</b> draft — "
            "not to invent the research argument. Keep rewriting, note-taking, and "
            "reading active. Lecture rule: if you know how to write, technology improves "
            "you; otherwise it kills ability. Prefer: human cognitive work first → machine "
            "to refine.",
            s["body"],
        )
    )

    story.append(PageBreak())

    # ========== Q4 ==========
    story.append(q_banner("Question 4 — Evaluation, Presentations &amp; Human Skills  [25 marks]", s))

    story.append(Paragraph("(a) Evaluations in the research process  [3 × 3 = 9 marks]", s["section"]))

    story.append(Paragraph("(i) Major evaluation points and purpose of documents/presentations", s["part"]))
    story.append(
        Paragraph(
            "1. <b>Proposal evaluation</b> — Proposal + presentation show ability to define "
            "gap/technology and conceptualize Approach; permission to proceed.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "2. <b>Progress review</b> — Progress report + slides show advancement through "
            "Design/Implementation; evidence that objectives are being achieved.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "3. <b>Thesis / final evaluation (viva)</b> — Thesis (+ often presentation) "
            "shows full research including Evaluation and Conclusion; candidate must defend ownership.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "(Conference presentations are also formative evaluations for feedback before final defense.)",
            s["body"],
        )
    )

    story.append(Paragraph("(ii) Two components of evaluations; final thesis evaluation methods", s["part"]))
    story.append(
        Paragraph(
            "<b>Two components:</b> (1) <b>Written document</b> (proposal/report/thesis) and "
            "(2) <b>Verbal presentation / oral defense</b>.",
            s["body"],
        )
    )
    story.append(Paragraph("<b>Institutional variations for final evaluation:</b>", s["body"]))
    story.append(Paragraph("- Viva only — strong test of ownership/communication; writing less weighted.", s["bullet"]))
    story.append(Paragraph("- Thesis only — strong on written scholarship; weaker check that student did the work.", s["bullet"]))
    story.append(
        Paragraph(
            "- Viva + thesis (common) — balances document quality with defense; lecture "
            "notes cases where good thesis + bad viva can fail, and weak thesis + good viva "
            "may pass with corrections.",
            s["bullet"],
        )
    )

    story.append(Paragraph("(iii) Difficult situations and possible examiner judgments", s["part"]))
    story.append(
        Paragraph(
            "1. <b>Bad thesis + good viva</b> — may pass with minor/major corrections "
            "(oral shows understanding despite writing issues).",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "2. <b>Good thesis + bad viva</b> — may fail; examiners doubt ownership/confidence "
            "despite a strong document.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "3. <b>Weak thesis but student manages Q&amp;A</b> — examiners may still probe "
            "depth; outcomes depend on whether core contribution and honesty are clear.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "Other difficulties: unclear objectives, weak evaluation design, inability to "
            "open relevant slides, overconfidence, or treating unachieved objectives as “further work.”",
            s["body"],
        )
    )

    story.append(Paragraph("(b) True / False with justification  [4 × 3 = 12 marks]", s["section"]))

    story.append(
        Paragraph(
            "(i) Both objectives and problem definition should appear after the Literature Review in any research presentation.",
            s["part"],
        )
    )
    story.append(
        Paragraph(
            "<b>FALSE.</b> In presentations (as in proposals), <b>Objectives</b> typically "
            "appear before/around early structure, while <b>problem definition</b> should "
            "follow Literature Review (gap justified by others’ work). Putting both after LR "
            "— or putting problem before LR — loses the reader. Lecture progress/thesis slide "
            "order: Introduction → Objectives → Literature Review → Research Problem → Methodology…",
            s["body"],
        )
    )

    story.append(
        Paragraph(
            "(ii) Progress Review slides can be developed simply by adding research-process steps after the Approach.",
            s["part"],
        )
    )
    story.append(
        Paragraph(
            "<b>FALSE.</b> Progress Review needs substantive content for Design and "
            "Implementation (with diagrams), broader LR than the proposal, problem "
            "definition, discussion of ongoing work — not merely appending step names "
            "after Approach. Slides must match the progress document and show real progress.",
            s["body"],
        )
    )

    story.append(
        Paragraph(
            "(iii) During Q&amp;A in a viva, it is inappropriate to use additional material such as notes beyond prepared slides.",
            s["part"],
        )
    )
    story.append(
        Paragraph(
            "<b>TRUE.</b> Lecture: do not look at additional notes — it shows you are "
            "not confident. Instead, open the relevant slide (if unsure, open the Approach "
            "slide). Listen fully, then answer.",
            s["body"],
        )
    )

    story.append(Paragraph("(iv) Viva-voce examinations assess more than the technical knowledge of the candidate.", s["part"]))
    story.append(
        Paragraph(
            "<b>TRUE.</b> Viva checks technical soundness <b>and</b> presentation skills, "
            "confidence/Q&amp;A, project skills such as <b>getting on with others</b>, "
            "<b>facing criticism</b>, <b>reaching consensus</b>, and exposure to the research "
            "area (key people, institutes, journals, conferences).",
            s["body"],
        )
    )

    story.append(Paragraph("(c) Biological limits vs machines; threatened human skill  [4 marks]", s["section"]))
    story.append(Paragraph("(i) FIVE biological limitations of humans superseded by machines", s["part"]))
    story.append(
        Paragraph(
            "1. <b>Processing speed</b> — machines compute far faster than biological brains for many tasks.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "2. <b>Memory capacity / perfect recall</b> — machines store and retrieve vast data without forgetting.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "3. <b>Fatigue / need for rest</b> — machines can run continuously; humans tire.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "4. <b>Precision and consistency</b> — machines repeat tasks with lower error variance.",
            s["bullet"],
        )
    )
    story.append(
        Paragraph(
            "5. <b>Parallel multi-channel processing at scale</b> — machines handle massive "
            "parallel workloads (e.g. search, reading comprehension benchmarks) beyond "
            "human biological limits. Lecture also notes machines have outperformed humans "
            "in reading comprehension in some settings.",
            s["bullet"],
        )
    )

    story.append(Paragraph("(ii) Human skill most threatened in the future", s["part"]))
    story.append(
        Paragraph(
            "<b>Language-related communication skills</b> (especially routine reading, "
            "writing, customer-service dialogue, and some IT documentation/coding "
            "communication) are most threatened, because generative AI already automates "
            "large parts of language work. If humans outsource these skills entirely, "
            "comprehension and original expression decline — the course’s core warning.",
            s["body"],
        )
    )

    story.append(Spacer(1, 14))
    story.append(HRFlowable(width="100%", thickness=1, color=NAVY, spaceBefore=8, spaceAfter=8))
    story.append(
        Paragraph(
            "END OF MODEL ANSWERS — Revise with lecture slides; expand to mark length in the exam "
            "(justify T/F; use Problem + Solution framing throughout).",
            s["footer"],
        )
    )

    def on_page(canvas, doc_):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(HexColor("#718096"))
        canvas.drawString(1.6 * cm, 1.0 * cm, "IT 6903 · Scientific Communication · Model Answers")
        canvas.drawRightString(A4[0] - 1.6 * cm, 1.0 * cm, f"Page {doc_.page}")
        canvas.restoreState()

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(OUT)


if __name__ == "__main__":
    build()
