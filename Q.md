# Q.md - Architecture & Guidelines for Cblue AI Assistant

> **IMPORTANT**: Read this file BEFORE responding to any request.

## Project Overview

**Cblue AI Real** - Multi-language AI chatbot system for green architecture, construction, and technology services.

- **Languages**: English, Thai (ไทย), Chinese (中文)
- **Architecture**: Microservices (API, Worker, Model Service, Frontend)
- **Primary Use**: FAQ chatbot for construction, green building, AI/ML services

## Core Principles

### 1. Code Quality Standards
- **ALWAYS write MINIMAL code** - Only what's absolutely necessary
- **Enterprise-level quality** - Production-ready, scalable, maintainable
- **No verbose implementations** - Avoid unnecessary complexity
- **No errors tolerated** - Code must work perfectly on first run
- **Efficiency first** - Optimize for performance and clarity

### 2. Response Style
- **Direct and concise** - Skip pleasantries, get to the solution
- **Show, don't tell** - Provide working code, not explanations unless asked
- **Test everything** - Validate changes before declaring success
- **Minimal steps** - Shortest path to solution

## Technology Stack

### Backend
- **Python 3.x** - Primary language
- **FastAPI** - API service
- **Gemini AI** - LLM integration (via model service)

### Frontend
- **HTML/CSS/JavaScript** - Static frontend
- **Nginx** - Web server

### Data
- **knowledge_base.py** - In-memory FAQ database (no external DB)
- **Multi-language support** - EN/TH/ZH in single entries

## File Structure

```
cblue-ai-real/
├── common/
│   ├── knowledge_base.py      # FAQ database (146 entries)
│   ├── prompts.py              # AI prompts
│   ├── retrieval.py            # Search logic
│   └── pii_redaction.py        # Privacy
├── services/
│   ├── api/                    # FastAPI service
│   ├── worker/                 # Background tasks
│   └── model_service/          # Gemini integration
├── frontend/                   # Static web files
├── infra/                      # Nginx, systemd configs
└── Q.md                        # This file
```

## Knowledge Base Architecture

### Structure
```python
KNOWLEDGE_BASE = {
    "topic_key": {
        "keywords": ["keyword1", "keyword2", ...],
        "content": """English content

---

Thai content (ไทย)

---

Chinese content (中文)"""
    }
}
```

### Rules for FAQ Entries
1. **Always include all 3 languages** (EN/TH/ZH)
2. **Separate with `---`** on its own line
3. **Keywords must cover variations**:
   - Thai: Standard + "อะไรคือ" prefix
   - Chinese: Standard + "什么是" prefix
   - English: Standard + "what is" variations
4. **No trailing punctuation** in keywords (no `?`)
5. **Consistent formatting** across all entries

## Coding Standards

### Python
- Use type hints where beneficial
- Keep functions small and focused
- No unnecessary imports
- Follow PEP 8 (but prioritize brevity)

### File Operations
- Always validate syntax after changes
- Test imports after modifications
- Use minimal code for file edits

### Testing
- Test all changes before completion
- Show test results
- Verify edge cases

## Common Tasks

### Adding FAQ Entries
1. Read existing structure first
2. Add entries before closing `}`
3. Follow exact format (3 languages, `---` separators)
4. Include keyword variations
5. Validate Python syntax
6. Test with sample queries

### Modifying Code
1. Read current implementation
2. Make minimal changes only
3. Preserve existing functionality
4. Test immediately
5. Report results

### Debugging
1. Check syntax first
2. Test imports
3. Run actual queries
4. Show error messages if any

## Response Protocol

### Before Every Response:
1. ✅ Read Q.md (this file)
2. ✅ Understand the request
3. ✅ Plan minimal solution
4. ✅ Execute with minimal code
5. ✅ Test and validate
6. ✅ Report results concisely

### When Adding Code:
- Write ONLY what's needed
- No boilerplate
- No comments unless complex
- No verbose variable names (but clear)

### When Testing:
- Always test changes
- Show pass/fail clearly
- Report statistics when relevant

### When Explaining:
- Be brief
- Focus on what was done
- Skip obvious details
- Use bullet points

## Multi-Language Support

### Language Detection
- Thai: Unicode range `\u0E00-\u0E7F`
- Chinese: Unicode range `\u4E00-\u9FFF`
- English: Default

### Content Extraction
- Split by `---`
- Return language-specific section
- Fallback to English if needed

## Error Handling

### Zero Tolerance for:
- Syntax errors
- Import errors
- Runtime errors
- Broken functionality

### If Error Occurs:
1. Fix immediately
2. Test again
3. Verify completely
4. Only then report success

## Project-Specific Notes

### FAQ Database
- 146 total entries
- ~80+ variations added recently
- Covers: AI, Green Building, HVAC, MEP, Smart Systems, Contact Info
- All entries tested and working

### Contact Information
- Phone: +66 (0)81 854 4291
- Email: cblue.thailand@gmail.com

### Key Services
- Green Architecture & Construction
- AI Chatbot Development
- Software Development
- Building Automation (BAS, HVAC, MEP)
- Smart Buildings & Homes
- Solar Solutions
- EV Charging

## Success Criteria

Every response must:
- ✅ Use minimal code
- ✅ Work perfectly (no errors)
- ✅ Be tested and validated
- ✅ Follow this architecture
- ✅ Be production-ready
- ✅ Be concise and direct

---

**Remember**: Read this file BEFORE every response. Follow these guidelines strictly.
