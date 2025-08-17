import re

I = re.IGNORECASE

patterns = [
    # ====== Identity ======
    (re.compile(r".*\b(who are you|what is your name|introduce yourself)\b.*", re.IGNORECASE),
     ["I'm Marqab (مرقب) — your startup lookout bot. I scan companies and funding stages to give quick, useful briefs."]),

    # ====== Companies (expanded briefs) ======
    (re.compile(r".*\b(who is|tell me about|give info about)\s+lean\b.*", re.IGNORECASE),
    ["Lean Technologies is a Saudi fintech startup founded in 2019. It provides APIs that allow developers and financial institutions to securely access bank data and initiate payments. Lean plays a key role in enabling open banking across the Middle East."]),

    (re.compile(r".*\b(who is|tell me about|give info about)\s+foodics\b.*", re.IGNORECASE),
    ["Foodics, founded in 2014 in Saudi Arabia, is a leading cloud-based point-of-sale (POS) and restaurant management platform. It offers solutions for payments, inventory, employee management, and analytics. Foodics has expanded across the MENA region, empowering thousands of restaurants."]),

    (re.compile(r".*\b(who is|tell me about|give info about)\s+salla\b.*", re.IGNORECASE),
    ["Salla is a Saudi e-commerce platform that enables entrepreneurs and businesses to build and manage their online stores without technical expertise. It provides integrated tools for payments, shipping, and marketing. Salla has become one of the most popular e-commerce enablers in Saudi Arabia."]),

    (re.compile(r".*\b(who is|tell me about|give info about)\s+nana\b.*", re.IGNORECASE),
    ["Nana is a Saudi-based online grocery delivery platform founded in 2016. It connects users with supermarkets and local stores, offering a wide range of products with home delivery. Nana has grown rapidly, especially during the COVID-19 pandemic, to become a leader in digital grocery shopping in KSA."]),

    (re.compile(r".*\b(who is|tell me about|give info about)\s+mozn\b.*", re.IGNORECASE),
    ["Mozn is a Saudi artificial intelligence and data analytics company. It builds machine learning and data-driven solutions for sectors such as finance, cybersecurity, and government. Mozn is also known for its RegTech products that help institutions comply with regulations like AML (Anti-Money Laundering)."]),

    (re.compile(r".*\b(who is|tell me about|give info about)\s+rewaa\b.*", re.IGNORECASE),
    ["Rewaa is a Saudi retail-tech startup offering cloud-based inventory and point-of-sale (POS) management systems. It helps retailers unify their sales channels, whether in-store or online, with real-time tracking. Rewaa has onboarded thousands of retailers across the region."]),

    (re.compile(r".*\b(who is|tell me about|give info about)\s+zid\b.*", re.IGNORECASE),
    ["Zid is a Saudi e-commerce platform founded in 2017. It helps merchants launch, manage, and scale their online stores with integrated tools for payments, logistics, and marketing. Zid has played a major role in driving e-commerce adoption among SMEs in Saudi Arabia."]),

    (re.compile(r".*\b(who is|tell me about|give info about)\s+classera\b.*", re.IGNORECASE),
    ["Classera is an EdTech company providing AI-driven learning management systems (LMS). It serves schools, universities, and training institutions with smart, gamified, and social learning tools. Classera has grown globally and is used by millions of learners in the Middle East, Africa, and beyond."]),

    (re.compile(r".*\b(who is|tell me about|give info about)\s+gathern\b.*", re.IGNORECASE),
    ["Gathern is a Saudi peer-to-peer accommodation marketplace. It allows users to book vacation rentals, chalets, farms, and resorts directly from property owners. Gathern has become one of the leading platforms for short-term rentals in Saudi Arabia."]),

    (re.compile(r".*\b(who is|tell me about|give info about)\s+sary\b.*", re.IGNORECASE),
    ["Sary is a B2B marketplace based in Saudi Arabia, connecting small businesses with wholesalers and suppliers. It enables bulk purchasing with better prices, faster delivery, and financing options. Sary plays a key role in digitizing supply chains in the region."]),


    # ====== Stages (your phrasing: 'explain stage X' / 'what is stage X') ======
    (re.compile(r".*\b(explain\s+stage\s+pre[-\s]?seed|what\s+is\s+stage\s+pre[-\s]?seed)\b.*", re.IGNORECASE),
     ["Pre-seed: earliest validation (idea/MVP), tiny checks (founders/FFF), early customer discovery."]),
    (re.compile(r".*\b(explain\s+stage\s+seed|what\s+is\s+stage\s+seed)\b.*", re.IGNORECASE),
     ["Seed: initial funding to prove product-market fit, hire core team, and grow early traction."]),
    (re.compile(r".*\b(explain\s+stage\s+series\s*a|what\s+is\s+stage\s+series\s*a)\b.*", re.IGNORECASE),
     ["Series A: scale what works — expand team, solidify go-to-market, grow users/revenue."]),
    (re.compile(r".*\b(explain\s+stage\s+series\s*b|what\s+is\s+stage\s+series\s*b)\b.*", re.IGNORECASE),
     ["Series B: accelerate growth — larger round for market expansion and process maturity."]),
    (re.compile(r".*\b(explain\s+stage\s+series\s*c|what\s+is\s+stage\s+series\s*c)\b.*", re.IGNORECASE),
     ["Series C: late growth & moats — global expansion, potential M&A, IPO prep."]),
    (re.compile(r".*\b(explain\s+stage\s+angel|what\s+is\s+stage\s+angel)\b.*", re.IGNORECASE),
     ["Angel: early backing from individual investors/syndicates with small checks."]),
    (re.compile(r".*\b(explain\s+stage\s+bridge|what\s+is\s+stage\s+bridge)\b.*", re.IGNORECASE),
     ["Bridge: interim round to extend runway to a milestone between major rounds."]),
    (re.compile(r".*\b(explain\s+stage\s+growth|what\s+is\s+stage\s+growth)\b.*", re.IGNORECASE),
     ["Growth: post-PMF scaling; capital fuels efficiency, expansion, and market leadership."]),
    (re.compile(r".*\b(explain\s+stage\s+bootstrapped|what\s+is\s+stage\s+bootstrapped)\b.*", re.IGNORECASE),
     ["Bootstrapped: self-funded growth from revenue/savings; no external equity."]),

    # ====== List stages ======
    (re.compile(r".*\b(what\s+are\s+(the\s+)?(funding|startup)\s+stages|list\s+(the\s+)?(funding|startup)\s+stages)\b.*", I),
     ["Stages: Pre-seed → Seed → Series A → Series B → Series C+ → Growth. Also seen: Angel, Bridge, Bootstrapped."]),

    # ====== Fallback (keep last) ======
    (re.compile(r".*", I),
     ["Sorry, I don't have enough information about your question, but don't worry — with Marqab, no one needs to be afraid!"
]),
]
