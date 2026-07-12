import os
import json
import re

def parse_yaml_frontmatter(content):
    """
    Simple robust YAML frontmatter parser to avoid external dependencies.
    Extracts title, description, tags, etc.
    """
    metadata = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            for line in frontmatter.split('\n'):
                if ':' in line:
                    key, val = line.split(':', 1)
                    key = key.strip().lower()
                    val = val.strip().strip('"').strip("'")
                    metadata[key] = val
    return metadata

def categorize_skill(name, desc):
    name_l = name.lower()
    desc_l = desc.lower() if desc else ""
    
    # 1. Cybersecurity & Hardening
    if any(k in name_l or k in desc_l for k in ['security', 'pentest', 'vulnerability', 'hack', 'privilege', 'exploit', 'cybersec', 'zero-trust', 'xss', 'injection', 'red-team', 'audit']):
        return 'Cybersecurity & Hardening'
        
    # 2. AI & Agentics
    if any(k in name_l or k in desc_l for k in ['agent', 'orchestrator', 'prompt', 'llm', 'claude', 'gemini', 'openai', 'think', 'agi', 'cogen', 'mcp']):
        return 'AI & Agentics'
        
    # 3. Data & Operations
    if any(k in name_l or k in desc_l for k in ['data', 'db', 'database', 'sql', 'postgresql', 'sqlite', 'xlsx', 'excel', 'csv', 'sheet', 'bigquery', 'tables']):
        return 'Data & Operations'
        
    # 4. Marketing & Growth
    if any(k in name_l or k in desc_l for k in ['marketing', 'seo', 'geo', 'sales', 'funnel', 'copywriting', 'ads', 'brand', 'social', 'linkedin', 'twitter', 'instagram', 'facebook', 'growth', 'audience']):
        return 'Marketing & Growth'
        
    # 5. Software Development
    if any(k in name_l or k in desc_l for k in ['development', 'coding', 'programming', 'api', 'framework', 'git', 'script', 'ts', 'js', 'python', 'rust', 'docker', 'deploy', 'pipeline', 'workflow', 'automation', 'wordpress']):
        return 'Software Development'
        
    # 6. Productivity & Utilities
    if any(k in name_l or k in desc_l for k in ['utility', 'helper', 'audio', 'video', 'convert', 'file', 'format', 'download', 'slack', 'zoom', 'notion', 'google', 'confluence', 'jira', 'calendar', 'email']):
        return 'Productivity & Utilities'
        
    return 'General Purpose'

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skills_dir = os.path.join(base_dir, 'skills')
    
    if not os.path.exists(skills_dir):
        print(f"Skills directory does not exist: {skills_dir}")
        return
        
    compiled_skills = []
    categories = {
        'AI & Agentics': [],
        'Marketing & Growth': [],
        'Cybersecurity & Hardening': [],
        'Software Development': [],
        'Data & Operations': [],
        'Productivity & Utilities': [],
        'General Purpose': []
    }
    
    print("Indexing all custom skills...")
    for skill_name in sorted(os.listdir(skills_dir)):
        skill_path = os.path.join(skills_dir, skill_name)
        if not os.path.isdir(skill_path):
            continue
            
        skill_md_path = os.path.join(skill_path, 'SKILL.md')
        if not os.path.exists(skill_md_path):
            continue
            
        try:
            with open(skill_md_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            metadata = parse_yaml_frontmatter(content)
            title = metadata.get('name', skill_name.replace('-', ' ').title())
            desc = metadata.get('description', '')
            
            # If description is missing, extract the first paragraph of body
            if not desc:
                parts = content.split('---')
                body = parts[-1].strip() if len(parts) >= 3 else content.strip()
                # strip out title headers
                body_clean = re.sub(r'^#+.*$', '', body, flags=re.MULTILINE).strip()
                lines = [l.strip() for l in body_clean.split('\n') if l.strip()]
                if lines:
                    desc = lines[0][:150] + '...' if len(lines[0]) > 150 else lines[0]
            
            category = categorize_skill(skill_name, desc)
            
            skill_info = {
                'id': skill_name,
                'name': title,
                'description': desc,
                'category': category,
                'path': f"skills/{skill_name}/SKILL.md"
            }
            
            compiled_skills.append(skill_info)
            categories[category].append(skill_info)
            
        except Exception as e:
            print(f"Error parsing {skill_name}: {str(e)}")
            
    # Write skills.json
    json_path = os.path.join(base_dir, 'skills.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(compiled_skills, f, indent=2, ensure_ascii=False)
    print(f"Successfully wrote {len(compiled_skills)} skills to skills.json")
    
    # Generate README.md
    readme_path = os.path.join(base_dir, 'README.md')
    
    stats_markdown = ""
    for cat, items in categories.items():
        if items:
            stats_markdown += f"- **{cat}**: {len(items)} skills\n"
            
    categories_tables = ""
    for cat, items in categories.items():
        if not items:
            continue
            
        categories_tables += f"\n### 📂 {cat} ({len(items)} skills)\n\n"
        categories_tables += "| Skill Name | Description | Path |\n"
        categories_tables += "|:---|:---|:---|\n"
        for item in items[:15]: # Show first 15 in README to keep length optimal, link to files
            desc_clean = item['description'].replace('\n', ' ').strip()
            categories_tables += f"| **{item['name']}** | {desc_clean} | [`{item['id']}`]({item['path']}) |\n"
            
        if len(items) > 15:
            categories_tables += f"| *And {len(items) - 15} more...* | *See the full list in [skills.json](skills.json)* | |\n"
            
    readme_content = f"""# 🌌 Jukeyman Skills System

> **Curated & Hardened by:** Rick Jefferson | RJ Business Solutions  
> **Total Active Intelligence Modules:** **{len(compiled_skills)} Custom Skills**

Welcome to the **Jukeyman Skills System** — the absolute premium, enterprise-hardened AI Agent playbook and execution engine. This repository acts as your decentralized local and cloud Second Brain, fully prepared to power any autonomous worker lifecycle.

---

## 📊 Knowledge Base Stats
{stats_markdown}

---

## 🛠️ CLI Sync & Deployment

### Sync to Current Project
To sync your jukeyman-skills directly into your active project for AI Agent discovery, run:
```bash
gsk init-skills
```

### Manual Git Pull
```bash
git pull origin main
```

---

## 🏛️ Categorized Intelligence Index

This directory lists your premium custom skills and agents categorized into high-value domains.

{categories_tables}

---

*Report compiled and maintained automatically by the Antigravity Master Compiler.*
"""

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("Successfully compiled README.md")

if __name__ == '__main__':
    main()
