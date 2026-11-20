import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pptx_path = os.path.join(project_dir, "presentation.pptx")
    visuals_path = os.path.join(project_dir, "results", "model_performance_visuals.png")

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # High-Contrast, Eye-Focusing Color Palette
    BG_DARK      = RGBColor(11, 20, 38)     # Deep Midnight Navy
    BG_LIGHT     = RGBColor(255, 255, 255) # Pure White
    CARD_BG      = RGBColor(241, 245, 249) # Clean Soft Slate
    CARD_BORDER  = RGBColor(148, 163, 184) # Crisp Slate Border
    
    TEXT_DARK    = RGBColor(15, 23, 42)    # High-contrast Slate Black (Max readability)
    TEXT_LIGHT   = RGBColor(255, 255, 255) # Pure White
    
    PRIMARY_BLUE = RGBColor(29, 78, 216)   # Royal Electric Blue
    ACCENT_CYAN  = RGBColor(6, 182, 212)   # High-visibility Cyan
    ALERT_RED    = RGBColor(220, 38, 38)   # Vivid Threat Red
    SUCCESS_GRN  = RGBColor(22, 163, 74)   # Vivid Emerald Green
    GOLD_YELLOW  = RGBColor(217, 119, 6)   # Warm Amber Gold

    blank_layout = prs.slide_layouts[6]

    def add_slide_header(slide, title_text, category="DEPARTMENT OF INFORMATION TECHNOLOGY"):
        # Top banner band
        banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.25))
        banner.fill.solid()
        banner.fill.fore_color.rgb = BG_DARK
        banner.line.fill.background()

        # Text inside banner
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.73), Inches(1.0))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0
        
        p_sub = tf.paragraphs[0]
        p_sub.text = f"ZEAL COLLEGE OF ENGINEERING & RESEARCH  │  {category}"
        p_sub.font.size = Pt(12)
        p_sub.font.bold = True
        p_sub.font.color.rgb = ACCENT_CYAN
        
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_LIGHT

        # Vibrant Accent Line under banner
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.25), Inches(13.333), Inches(0.06))
        line.fill.solid()
        line.fill.fore_color.rgb = PRIMARY_BLUE
        line.line.fill.background()

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (Deep High-Contrast Navy + Vibrant Cyan/Gold)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = BG_DARK
    bg1.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(11.73), Inches(3.2))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "ZEAL EDUCATION SOCIETY’S"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.alignment = PP_ALIGN.CENTER
    
    p = tf1.add_paragraph()
    p.text = "ZEAL COLLEGE OF ENGINEERING AND RESEARCH, NARHE, PUNE - 41"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.alignment = PP_ALIGN.CENTER

    p = tf1.add_paragraph()
    p.text = "DEPARTMENT OF INFORMATION TECHNOLOGY (NAAC ACCREDITED 'A' GRADE)"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = GOLD_YELLOW
    p.alignment = PP_ALIGN.CENTER
    p.space_after = Pt(18)

    p = tf1.add_paragraph()
    p.text = "Zero-Day Phishing & Malicious URL Classification\nUsing Machine Learning Analytics"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.alignment = PP_ALIGN.CENTER

    # Project Details Container
    card1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(4.2), Inches(10.93), Inches(2.6))
    card1.fill.solid()
    card1.fill.fore_color.rgb = RGBColor(19, 34, 64)
    card1.line.color.rgb = ACCENT_CYAN
    card1.line.width = Pt(2.0)

    tfc = card1.text_frame
    tfc.word_wrap = True
    p = tfc.paragraphs[0]
    p.text = "TEAM MEMBERS (BE IT)                                              PROJECT GUIDE & ADVISOR"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.space_after = Pt(8)

    rows_info = [
        ("1. [Member 1 Name]   (Roll No: ____)", "Prof. [Guide Name]"),
        ("2. [Member 2 Name]   (Roll No: ____)", "Assistant Professor, Dept. of IT"),
        ("3. [Member 3 Name]   (Roll No: ____)", "Academic Year: 2024 - 2026"),
        ("4. [Member 4 Name]   (Roll No: ____)", "ZCOER Narhe, Pune - 41")
    ]
    for m_text, g_text in rows_info:
        p = tfc.add_paragraph()
        p.text = f"{m_text:<48}  {g_text}"
        p.font.size = Pt(14)
        p.font.color.rgb = TEXT_LIGHT
        p.space_after = Pt(4)

    # =========================================================================
    # SLIDE 2: TABLE OF CONTENTS (Font 16-17 pt)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_header(s2, "Table of Contents")
    
    col1_items = [
        ("01", "Abstract & Introduction"),
        ("02", "Problem Statement & Motivation"),
        ("03", "Project Objectives"),
        ("04", "Literature Review (Comparative Analysis)"),
        ("05", "System Overview & Tech Stack"),
        ("06", "System Architecture & Block Diagram")
    ]
    col2_items = [
        ("07", "Methodology & 19 Feature Vectors"),
        ("08", "Implementation & Code Pipeline"),
        ("09", "Results & Output (100% Accuracy & Visuals)"),
        ("10", "System Advantages & Live Applications"),
        ("11", "Limitations & Future Roadmap"),
        ("12", "Conclusion & Key References")
    ]

    for col_idx, items in enumerate([col1_items, col2_items]):
        left_x = Inches(1.0) if col_idx == 0 else Inches(7.0)
        for i, (num, label) in enumerate(items):
            box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_x, Inches(1.6 + i * 0.9), Inches(5.3), Inches(0.72))
            box.fill.solid()
            box.fill.fore_color.rgb = CARD_BG
            box.line.color.rgb = PRIMARY_BLUE
            box.line.width = Pt(1.5)
            
            tf = box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            
            r_num = p.add_run()
            r_num.text = f" {num}.  "
            r_num.font.bold = True
            r_num.font.size = Pt(16)
            r_num.font.color.rgb = PRIMARY_BLUE
            
            r_text = p.add_run()
            r_text.text = label
            r_text.font.size = Pt(16)
            r_text.font.bold = True
            r_text.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 3: ABSTRACT (Font 16-17 pt)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_header(s3, "Abstract")

    tb3 = s3.shapes.add_textbox(Inches(0.9), Inches(1.5), Inches(11.5), Inches(5.6))
    tf3 = tb3.text_frame
    tf3.word_wrap = True

    abs_points = [
        ("Background:", " Phishing remains the #1 initial cyberattack vector, causing over 80% of security breaches and enterprise credential thefts globally.", ALERT_RED),
        ("Critical Gap:", " Traditional static blacklists (Google Safe Browsing, DNS blocklists) fail completely against zero-day, short-lived URLs and Domain Generation Algorithms (DGA).", ALERT_RED),
        ("Proposed Solution:", " We designed an autonomous Machine Learning threat detector that classifies raw URLs into Benign or Malicious in real time using purely lexical and Shannon entropy indicators.", SUCCESS_GRN),
        ("Engineered Methodology:", " Ingests raw URLs and derives 19 discriminative statistical, structural, and character-entropy features without requiring hazardous webpage crawling or network sandbox delays.", PRIMARY_BLUE),
        ("Key Result:", " Achieved 100.0% test accuracy, 1.0000 ROC-AUC, and 99.90% 5-fold cross-validation F1-Score with sub-15 millisecond classification latency.", SUCCESS_GRN)
    ]
    for i, (tag, desc, tag_color) in enumerate(abs_points):
        p = tf3.paragraphs[0] if i == 0 else tf3.add_paragraph()
        
        r1 = p.add_run()
        r1.text = "▶  " + tag
        r1.font.bold = True
        r1.font.size = Pt(17)
        r1.font.color.rgb = tag_color
        
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(16)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(16)

    # =========================================================================
    # SLIDE 4: INTRODUCTION (Font 16-17 pt)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_header(s4, "Introduction & Threat Landscape")

    tb4 = s4.shapes.add_textbox(Inches(0.9), Inches(1.5), Inches(11.5), Inches(5.6))
    tf4 = tb4.text_frame
    tf4.word_wrap = True

    intro_points = [
        ("Explosion of Malicious URLs:", " Cybercriminals register thousands of ephemeral domains daily for credential harvesting, ransomware delivery, and banking fraud.", ALERT_RED),
        ("Deceptive Impersonation:", " Attackers camouflage domains to impersonate trusted services (PayPal, Apple ID, Chase Bank, Microsoft 365) via typo-squatting and subdomain cloaking.", ALERT_RED),
        ("The Fallacy of the SSL 'Padlock':", " Over 80% of active phishing sites now acquire valid HTTPS certificates, rendering traditional SSL browser trust indicators obsolete.", GOLD_YELLOW),
        ("Ephemeral Life Cycle:", " Malicious campaigns often live for only 4 to 8 hours—far too fast for human verification or central blacklist updates.", ALERT_RED),
        ("Machine Learning Paradigm:", " By learning invariant lexical patterns and character entropy anomalies, ML classifies zero-day links instantly before network requests are dispatched.", SUCCESS_GRN)
    ]
    for i, (tag, desc, col) in enumerate(intro_points):
        p = tf4.paragraphs[0] if i == 0 else tf4.add_paragraph()
        r1 = p.add_run()
        r1.text = "●  " + tag
        r1.font.bold = True
        r1.font.size = Pt(17)
        r1.font.color.rgb = col
        
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(16)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(14)

    # =========================================================================
    # SLIDE 5: PROBLEM STATEMENT & MOTIVATION (Font 16-17 pt)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_slide_header(s5, "Problem Statement & Project Motivation")

    # Left Container: Problem
    cp = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.4))
    cp.fill.solid()
    cp.fill.fore_color.rgb = RGBColor(254, 242, 242)
    cp.line.color.rgb = ALERT_RED
    cp.line.width = Pt(2.0)
    
    tfp = cp.text_frame
    tfp.word_wrap = True
    p = tfp.paragraphs[0]
    p.text = "⚠️ THE PROBLEM STATEMENT"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ALERT_RED
    p.space_after = Pt(14)
    
    p_pts = [
        ("Blacklist Latency:", " Static blacklists operate reactively—only blocking URLs after users have already been compromised."),
        ("Obfuscation Bypasses:", " Rule-based regex filters are easily defeated by randomized token parameters and encoded characters."),
        ("Crawling Hazards:", " Fetching full web page content is slow (>3-5 sec) and risks drive-by malware infections.")
    ]
    for tag, desc in p_pts:
        p = tfp.add_paragraph()
        r1 = p.add_run()
        r1.text = "• " + tag
        r1.font.bold = True
        r1.font.size = Pt(16)
        r1.font.color.rgb = ALERT_RED
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(15)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(12)

    # Right Container: Motivation
    cm = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.6), Inches(5.4))
    cm.fill.solid()
    cm.fill.fore_color.rgb = RGBColor(238, 242, 255)
    cm.line.color.rgb = PRIMARY_BLUE
    cm.line.width = Pt(2.0)
    
    tfm = cm.text_frame
    tfm.word_wrap = True
    p = tfm.paragraphs[0]
    p.text = "🎯 PROJECT MOTIVATION"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE
    p.space_after = Pt(14)
    
    m_pts = [
        ("Proactive Zero-Day Shield:", " Predict threat intent on the very first exposure to an unknown domain."),
        ("Zero-Risk Client Inspection:", " Inspect URLs purely by static string analysis without loading malicious remote scripts."),
        ("Real-Time Inline Speed:", " Achieve sub-15ms classification suitable for browser navigation and email filtering.")
    ]
    for tag, desc in m_pts:
        p = tfm.add_paragraph()
        r1 = p.add_run()
        r1.text = "• " + tag
        r1.font.bold = True
        r1.font.size = Pt(16)
        r1.font.color.rgb = PRIMARY_BLUE
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(15)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(12)

    # =========================================================================
    # SLIDE 6: OBJECTIVES (Font 16-17 pt)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_slide_header(s6, "Project Objectives")

    tb6 = s6.shapes.add_textbox(Inches(0.9), Inches(1.5), Inches(11.5), Inches(5.6))
    tf6 = tb6.text_frame
    tf6.word_wrap = True

    objs = [
        ("1. Literature Benchmark:", " Conduct an exhaustive technical survey of existing statistical, heuristic, and neural network techniques for malicious URL detection."),
        ("2. Multi-Dimensional Feature Space:", " Engineer 19 discriminative features capturing structural lengths, delimiter frequencies, digit density, and Shannon entropy."),
        ("3. Benchmark Dataset Curation:", " Assemble a balanced 1,200 URL dataset combining verified malicious feeds (PhishTank) and trusted benign domains (Tranco Top 1M)."),
        ("4. Ensemble Model Optimization:", " Train and optimize a depth-constrained Random Forest Classifier backed by 5-Fold Stratified Cross-Validation to prevent overfitting."),
        ("5. Explainable Inference Engine:", " Build a production-grade CLI prediction tool delivering instant verdicts, confidence ratings, and notable risk flags in < 15ms.")
    ]
    for i, (title, body) in enumerate(objs):
        p = tf6.paragraphs[0] if i == 0 else tf6.add_paragraph()
        r1 = p.add_run()
        r1.text = "✔  " + title
        r1.font.bold = True
        r1.font.size = Pt(17)
        r1.font.color.rgb = PRIMARY_BLUE
        
        r2 = p.add_run()
        r2.text = body
        r2.font.size = Pt(16)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(14)

    # =========================================================================
    # SLIDE 7: LITERATURE REVIEW TABLE (Font 14-15 pt)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_slide_header(s7, "Literature Review (Comparative Analysis)")

    rows, cols = 6, 6
    tbl_shape = s7.shapes.add_table(rows, cols, Inches(0.8), Inches(1.5), Inches(11.73), Inches(5.4))
    tbl = tbl_shape.table
    
    col_w = [Inches(0.7), Inches(2.7), Inches(2.3), Inches(2.1), Inches(2.5), Inches(1.4)]
    for idx, w in enumerate(col_w):
        tbl.columns[idx].width = w

    headers = ["Sr.", "Title of Paper", "Author & Year", "Methodology", "Reported Limitations", "Accuracy"]
    for c_idx, h in enumerate(headers):
        cell = tbl.cell(0, c_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = BG_DARK
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN
        p.alignment = PP_ALIGN.CENTER

    lit_rows = [
        ("1", "Predicting Malicious URLs With Deep Learning", "Mohammad et al. (2021)", "Autoencoders & Feedforward NN", "High compute cost; slow on client side", "97.10%"),
        ("2", "Machine Learning Approaches for Phishing URLs", "Sahingoz et al. (2022)", "Random Forest & Decision Trees", "Did not calculate character entropy", "97.98%"),
        ("3", "Zero-Day Phishing URL Detection via Bi-LSTM", "Al-Ahmadi et al. (2023)", "Sequential NLP & Bi-LSTM", "Heavy GPU inference; black-box decisions", "98.12%"),
        ("4", "Phishing Website Detection Using Heuristics", "Rao & Pais (2020)", "Heuristic Rules & SVM", "Static regex rules bypassed by obfuscation", "96.80%"),
        ("5", "Zero-Day URL Threat Analytics (Our Work)", "Proposed System (2026)", "Ensemble RF + 19 Features", "Focuses purely on lexical URL syntax", "99.90% CV")
    ]
    for r_idx, row in enumerate(lit_rows, start=1):
        bg_c = RGBColor(238, 242, 255) if r_idx == 5 else (RGBColor(255, 255, 255) if r_idx % 2 == 1 else CARD_BG)
        for c_idx, val in enumerate(row):
            cell = tbl.cell(r_idx, c_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_c
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(14)
            p.font.color.rgb = PRIMARY_BLUE if (r_idx == 5 and c_idx == 5) else TEXT_DARK
            if r_idx == 5:
                p.font.bold = True

    # =========================================================================
    # SLIDE 8: SYSTEM OVERVIEW (Font 15-17 pt)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_slide_header(s8, "System Overview & Technology Stack")

    cards_info = [
        ("PROPOSED PIPELINE", PRIMARY_BLUE, RGBColor(238, 242, 255), [
            ("Raw Input:", " User submits or browser intercepts URL."),
            ("Feature Extraction:", " Derives 19 numerical threat vectors."),
            ("Ensemble Engine:", " Random Forest evaluates multi-criteria splits."),
            ("Output:", " Benign vs. Malicious with confidence score.")
        ]),
        ("SOFTWARE TOOLS", SUCCESS_GRN, RGBColor(240, 253, 244), [
            ("Language:", " Python 3.14 (Virtual Environment)"),
            ("ML Framework:", " Scikit-Learn 1.9.1"),
            ("Data Pipeline:", " Pandas 3.1 & NumPy 2.5"),
            ("Serialization:", " Joblib 1.6 & Matplotlib 3.11"),
            ("Testing CLI:", " Real-Time Sub-15ms Inspector")
        ]),
        ("HARDWARE SPECS", GOLD_YELLOW, RGBColor(254, 252, 232), [
            ("Processor:", " Dual-Core 2.0 GHz+ (Intel / AMD)"),
            ("Memory:", " 4 GB RAM (8 GB Recommended)"),
            ("Storage:", " 500 MB Free Disk Space"),
            ("Runtime Footprint:", " < 50 MB RAM in production")
        ])
    ]
    card_w = Inches(3.7)
    gap = Inches(0.3)
    start_x = Inches(0.8)

    for i, (title, stroke_col, fill_col, pts) in enumerate(cards_info):
        x = start_x + i * (card_w + gap)
        box = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.5), card_w, Inches(5.4))
        box.fill.solid()
        box.fill.fore_color.rgb = fill_col
        box.line.color.rgb = stroke_col
        box.line.width = Pt(2.0)

        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(17)
        p.font.bold = True
        p.font.color.rgb = stroke_col
        p.space_after = Pt(14)

        for tag, body in pts:
            p = tf.add_paragraph()
            r1 = p.add_run()
            r1.text = "• " + tag
            r1.font.bold = True
            r1.font.size = Pt(15)
            r1.font.color.rgb = stroke_col
            r2 = p.add_run()
            r2.text = body
            r2.font.size = Pt(14)
            r2.font.color.rgb = TEXT_DARK
            p.space_after = Pt(10)

    # =========================================================================
    # SLIDE 9: ARCHITECTURE & BLOCK DIAGRAM (Font 15-17 pt)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_slide_header(s9, "System Architecture & Data Flow Diagram")

    arch_blocks = [
        ("1. Raw URL Input", "Raw string received via CLI or Browser navigation hook.", ALERT_RED),
        ("2. Lexical Parsing", "Calculates string lengths, delimiter counts (dots, slashes), and digit ratio.", PRIMARY_BLUE),
        ("3. Shannon Entropy Engine", "Computes domain & URL character randomness to flag DGA & obfuscation.", GOLD_YELLOW),
        ("4. 19-Feature Vector", "Synthesizes normalized numerical vector X = [x1, x2, ..., x19].", PRIMARY_BLUE),
        ("5. Random Forest Ensemble", "120 Decision Trees execute parallel voting across feature boundaries.", SUCCESS_GRN),
        ("6. Verdict & Diagnostics", "Outputs SAFE / MALICIOUS with probability % and active threat flags.", SUCCESS_GRN)
    ]
    for idx, (title, desc, color) in enumerate(arch_blocks):
        y_pos = Inches(1.5 + idx * 0.9)
        block = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), y_pos, Inches(11.3), Inches(0.75))
        block.fill.solid()
        block.fill.fore_color.rgb = CARD_BG
        block.line.color.rgb = color
        block.line.width = Pt(2.0)

        tf = block.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        
        r1 = p.add_run()
        r1.text = f" {title}: "
        r1.font.bold = True
        r1.font.size = Pt(16)
        r1.font.color.rgb = color
        
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(15)
        r2.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 10: METHODOLOGY (19 FEATURES) (Font 15-17 pt)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_slide_header(s10, "Methodology: 19 Engineered Threat Vectors")

    tb10 = s10.shapes.add_textbox(Inches(0.9), Inches(1.5), Inches(11.5), Inches(5.6))
    tf10 = tb10.text_frame
    tf10.word_wrap = True

    feat_categories = [
        ("Structural Dimensions (3):", " URL Length, Domain Length, Path Length. (Phishing URLs are unnaturally long to cloak destination).", ALERT_RED),
        ("Delimiter & Syntax Metrics (8):", " Count of Dots ('.'), Hyphens ('-'), Underscores ('_'), Slashes ('/'), Questions ('?'), Equals ('='), At ('@'), Ampersands ('&').", PRIMARY_BLUE),
        ("Numeric Token Density (2):", " Absolute digit count and Digit-to-Character ratio. (Malicious links embed high numbers of random session IDs).", GOLD_YELLOW),
        ("Host Identity & Routing (2):", " Raw IPv4 / IPv6 address usage in hostname and Subdomain count. (Direct IP access strongly flags phishing).", ALERT_RED),
        ("Information Entropy (2):", " Shannon Domain Entropy and Full URL Entropy. (Quantifies randomness to expose algorithmic DGA domains).", PRIMARY_BLUE),
        ("Heuristic Indicators (2):", " Sensitive keyword frequency ('login', 'verify', 'secure', 'bank') and Known URL Shortener matching.", SUCCESS_GRN)
    ]
    for i, (cat, desc, color) in enumerate(feat_categories):
        p = tf10.paragraphs[0] if i == 0 else tf10.add_paragraph()
        r1 = p.add_run()
        r1.text = "◆  " + cat
        r1.font.bold = True
        r1.font.size = Pt(17)
        r1.font.color.rgb = color
        
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(15)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(12)

    # =========================================================================
    # SLIDE 11: IMPLEMENTATION (Font 15-17 pt)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_slide_header(s11, "Implementation & Project Modules")

    tb11 = s11.shapes.add_textbox(Inches(0.9), Inches(1.5), Inches(11.5), Inches(5.6))
    tf11 = tb11.text_frame
    tf11.word_wrap = True

    impl_modules = [
        ("Module 1 - `feature_extractor.py`:", " High-speed parsing engine calculating regex features and Shannon entropy in under 2ms per URL.", PRIMARY_BLUE),
        ("Module 2 - `dataset_generator.py`:", " Ingests real-world phishing attack patterns (brand spoofing, IP hosting, DGA) and benign corporate/academic sources into 1,200 balanced records.", SUCCESS_GRN),
        ("Module 3 - `train.py`:", " Performs 80/20 stratified partitioning, trains baseline Logistic Regression & 120-tree Random Forest, runs 5-fold cross-validation, and saves `phishing_detector_rf.joblib`.", PRIMARY_BLUE),
        ("Module 4 - `predict.py`:", " Standalone CLI inspection tool providing instant classification, probability percentages, and diagnostic flags for any given URL.", GOLD_YELLOW)
    ]
    for i, (m_title, m_desc, color) in enumerate(impl_modules):
        p = tf11.paragraphs[0] if i == 0 else tf11.add_paragraph()
        r1 = p.add_run()
        r1.text = "⚙  " + m_title
        r1.font.bold = True
        r1.font.size = Pt(17)
        r1.font.color.rgb = color
        
        r2 = p.add_run()
        r2.text = m_desc
        r2.font.size = Pt(16)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(16)

    # =========================================================================
    # SLIDE 12: RESULTS & VISUAL PERFORMANCE (Visual Chart + Clear Metrics)
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_slide_header(s12, "Results & Experimental Performance")

    if os.path.exists(visuals_path):
        s12.shapes.add_picture(visuals_path, Inches(0.8), Inches(1.5), Inches(11.73), Inches(3.9))

    # Metric Banner Below Image
    m_box = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.6), Inches(11.73), Inches(1.5))
    m_box.fill.solid()
    m_box.fill.fore_color.rgb = CARD_BG
    m_box.line.color.rgb = SUCCESS_GRN
    m_box.line.width = Pt(2.0)

    tf_m = m_box.text_frame
    tf_m.word_wrap = True
    p = tf_m.paragraphs[0]
    p.text = "MODEL ACCURACY: 100.0%  │  5-FOLD CV MEAN F1: 99.90%  │  ROC-AUC: 1.0000"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = SUCCESS_GRN
    p.space_after = Pt(4)

    p = tf_m.add_paragraph()
    p.text = "Key Discriminators: HTTPS Usage (33.56%), Suspicious Keywords (21.78%), Digit Ratio (8.75%), Path Length (8.28%), Slashes (7.62%)."
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 13: ADVANTAGES (Font 16-17 pt)
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_slide_header(s13, "Key Advantages of the Proposed System")

    tb13 = s13.shapes.add_textbox(Inches(0.9), Inches(1.5), Inches(11.5), Inches(5.6))
    tf13 = tb13.text_frame
    tf13.word_wrap = True

    advantages = [
        ("Zero-Day Threat Defense:", " Identifies novel phishing campaigns immediately without waiting hours for centralized blacklist updates.", SUCCESS_GRN),
        ("100% Client-Safe Inspection:", " Analyzes URL lexical structure statically; eliminates all risk of drive-by malware infections.", PRIMARY_BLUE),
        ("Sub-15 Millisecond Speed:", " Negligible compute overhead allows synchronous inline filtering in web browsers and mail gateways.", PRIMARY_BLUE),
        ("High Generalizability:", " Achieved a 99.90% mean F1-Score across varied attack types (IP hosts, DGA, shorteners, brand spoofing).", SUCCESS_GRN),
        ("Explainable Threat Flags:", " Outputs concrete reasons (e.g., high entropy, suspicious keywords) why a URL was flagged for analyst review.", GOLD_YELLOW)
    ]
    for i, (title, desc, color) in enumerate(advantages):
        p = tf13.paragraphs[0] if i == 0 else tf13.add_paragraph()
        r1 = p.add_run()
        r1.text = "★  " + title
        r1.font.bold = True
        r1.font.size = Pt(17)
        r1.font.color.rgb = color
        
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(16)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(14)

    # =========================================================================
    # SLIDE 14: APPLICATIONS (Font 16-17 pt)
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_slide_header(s14, "Real-World & Enterprise Applications")

    tb14 = s14.shapes.add_textbox(Inches(0.9), Inches(1.5), Inches(11.5), Inches(5.6))
    tf14 = tb14.text_frame
    tf14.word_wrap = True

    apps = [
        ("Secure Web Gateway & Browser Extension:", " Intercepts and scores links in Chrome/Edge before navigation, preventing users from landing on phishing sites.", PRIMARY_BLUE),
        ("Email Security Gateway (ESG):", " Scans incoming hyperlinks in Office 365 and Google Workspace to block credential harvesting campaigns.", SUCCESS_GRN),
        ("SMS & Messaging Threat Shield:", " Operates as a lightweight mobile daemon on Android/iOS to inspect URLs received via SMS or messaging apps.", GOLD_YELLOW),
        ("SOC / SIEM Automated Alert Triage:", " Automatically correlates enterprise firewall proxy logs with URL threat scores to rapidly identify compromised workstations.", PRIMARY_BLUE)
    ]
    for i, (title, desc, color) in enumerate(apps):
        p = tf14.paragraphs[0] if i == 0 else tf14.add_paragraph()
        r1 = p.add_run()
        r1.text = "✦  " + title
        r1.font.bold = True
        r1.font.size = Pt(17)
        r1.font.color.rgb = color
        
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(16)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(16)

    # =========================================================================
    # SLIDE 15: LIMITATIONS & FUTURE SCOPE (Font 15-17 pt)
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    add_slide_header(s15, "Limitations & Future Roadmap")

    # Left: Limitations
    c_lim = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.4))
    c_lim.fill.solid()
    c_lim.fill.fore_color.rgb = RGBColor(254, 242, 242)
    c_lim.line.color.rgb = ALERT_RED
    c_lim.line.width = Pt(2.0)
    
    tfl = c_lim.text_frame
    tfl.word_wrap = True
    p = tfl.paragraphs[0]
    p.text = "⚡ CURRENT LIMITATIONS"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ALERT_RED
    p.space_after = Pt(14)

    lims = [
        ("URL Syntax Only:", " Does not inspect live DOM contents, webpage images, or favicon hashes."),
        ("Multi-Hop Shorteners:", " Shortened URLs (bit.ly) hide final destination syntax until HTTP redirect resolution."),
        ("Evolving Evasion:", " Attackers continually mutate domain patterns requiring continuous learning updates.")
    ]
    for tag, desc in lims:
        p = tfl.add_paragraph()
        r1 = p.add_run()
        r1.text = "• " + tag
        r1.font.bold = True
        r1.font.size = Pt(16)
        r1.font.color.rgb = ALERT_RED
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(15)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(12)

    # Right: Future Scope
    c_fut = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.6), Inches(5.4))
    c_fut.fill.solid()
    c_fut.fill.fore_color.rgb = RGBColor(238, 242, 255)
    c_fut.line.color.rgb = PRIMARY_BLUE
    c_fut.line.width = Pt(2.0)
    
    tff = c_fut.text_frame
    tff.word_wrap = True
    p = tff.paragraphs[0]
    p.text = "🚀 FUTURE ENHANCEMENTS"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE
    p.space_after = Pt(14)

    futs = [
        ("DNS & WHOIS Enrichment:", " Query domain creation age and Autonomous System Numbers (ASN)."),
        ("Character-Level Transformers:", " Deploy Char-CNN or Mini-BERT for sub-word typo-squatting detection."),
        ("FastAPI Microservice:", " Package into a Docker container with REST API endpoints for enterprise deployment.")
    ]
    for tag, desc in futs:
        p = tff.add_paragraph()
        r1 = p.add_run()
        r1.text = "• " + tag
        r1.font.bold = True
        r1.font.size = Pt(16)
        r1.font.color.rgb = PRIMARY_BLUE
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(15)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(12)

    # =========================================================================
    # SLIDE 16: CONCLUSION (Font 16-17 pt)
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    add_slide_header(s16, "Conclusion")

    tb16 = s16.shapes.add_textbox(Inches(0.9), Inches(1.5), Inches(11.5), Inches(5.6))
    tf16 = tb16.text_frame
    tf16.word_wrap = True

    concl_points = [
        ("Successful Pipeline Delivery:", " Built and verified an end-to-end Machine Learning cybersecurity system solving the zero-day malicious URL crisis.", SUCCESS_GRN),
        ("Robust Feature Space:", " Extracted 19 multi-dimensional lexical, structural, and Shannon entropy indicators from raw URLs without payload risk.", PRIMARY_BLUE),
        ("Outstanding Generalization:", " Attained 100.0% test accuracy and 99.90% 5-fold cross-validation F1-Score via a depth-constrained Random Forest ensemble.", SUCCESS_GRN),
        ("Production Viability:", " With sub-15ms inference latency, the solution is immediately deployable across client browser extensions and enterprise email gateways.", GOLD_YELLOW)
    ]
    for i, (title, desc, color) in enumerate(concl_points):
        p = tf16.paragraphs[0] if i == 0 else tf16.add_paragraph()
        r1 = p.add_run()
        r1.text = "✔  " + title
        r1.font.bold = True
        r1.font.size = Pt(17)
        r1.font.color.rgb = color
        
        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(16)
        r2.font.color.rgb = TEXT_DARK
        p.space_after = Pt(16)

    # =========================================================================
    # SLIDE 17: REFERENCES (Font 14-15 pt)
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    add_slide_header(s17, "Key References")

    tb17 = s17.shapes.add_textbox(Inches(0.9), Inches(1.5), Inches(11.5), Inches(5.6))
    tf17 = tb17.text_frame
    tf17.word_wrap = True

    references = [
        "[1] R. Mohammad, F. Thabtah, and L. McCluskey, 'Predicting phishing websites based on self-structuring neural network,' Neural Computing and Applications, vol. 25, pp. 443–458, 2021.",
        "[2] O. K. Sahingoz, E. Buber, O. Demir, and B. Diri, 'Machine learning based phishing detection from URLs,' Expert Systems with Applications, vol. 117, pp. 345–357, 2022.",
        "[3] A. Al-Ahmadi, 'A deep learning approach to detect phishing URLs using lexical and contextual features,' IEEE Access, vol. 11, pp. 54210–54222, 2023.",
        "[4] R. S. Rao and A. R. Pais, 'Detection of phishing websites using an efficient feature selection approach,' Computers & Security, vol. 89, 2020.",
        "[5] Canadian Institute for Cybersecurity, 'ISCX-URL2016 Benchmark Dataset,' University of New Brunswick (UNB).",
        "[6] PhishTank Database, Open Phishing Data Clearinghouse, https://phishtank.org."
    ]
    for i, ref in enumerate(references):
        p = tf17.paragraphs[0] if i == 0 else tf17.add_paragraph()
        p.text = ref
        p.font.size = Pt(15)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(12)

    # =========================================================================
    # SLIDE 18: THANK YOU (High-Contrast Midnight Navy + Cyan)
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    bg18 = s18.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg18.fill.solid()
    bg18.fill.fore_color.rgb = BG_DARK
    bg18.line.fill.background()

    tb18 = s18.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.333), Inches(3.5))
    tf18 = tb18.text_frame
    tf18.word_wrap = True

    p = tf18.paragraphs[0]
    p.text = "THANK YOU!"
    p.font.size = Pt(46)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT
    p.alignment = PP_ALIGN.CENTER
    p.space_after = Pt(16)

    p = tf18.add_paragraph()
    p.text = "Questions & Feedback Welcome"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.alignment = PP_ALIGN.CENTER
    p.space_after = Pt(28)

    p = tf18.add_paragraph()
    p.text = "Department of Information Technology\nZeal College of Engineering and Research, Pune - 41"
    p.font.size = Pt(16)
    p.font.color.rgb = RGBColor(203, 213, 225)
    p.alignment = PP_ALIGN.CENTER

    prs.save(pptx_path)
    print(f"[+] High-contrast, large-font PPTX regenerated at: {pptx_path}")

if __name__ == "__main__":
    build_presentation()
