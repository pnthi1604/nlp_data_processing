import pandas as pd
import re

def condition_length_with_tokenizer(
    tokenizer,
    text,
    min_len_token,
    max_len_token,
):
    if type(text) != str:
        return False
    text = tokenizer.encode(text).ids
    return len(text) >= min_len_token and len(text) <= max_len_token

def condition_non_number_character(text):
    if type(text) != str:
        return False
    if any(char.isdigit() for char in text):
        return False
    return True

def condition_min_max_length(text, min_len, max_len):
    if type(text) != str:
        return False
    return len(text.split()) >= min_len and len(text.split()) <= max_len


def condition_not_code_and_link(text):
    # Regular expressions for detecting URLs
    url_pattern = re.compile(r'http[s]?://\S+|www\.\S+')
    
    # Regular expressions for detecting code snippets (various languages)
    code_patterns = [
        re.compile(r'`[^`]*`'),  # Inline code using backticks
        re.compile(r'<code>[^<]*</code>', re.DOTALL),  # Code inside <code> tags
        re.compile(r'#include\s*<[^>]+>'),  # C++ #include directive
        re.compile(r'\bclass\b|\bdef\b|\bimport\b'),  # Python keywords
        re.compile(r'\bfunction\b|\bvar\b|\bconst\b|\blet\b'),  # JavaScript keywords
        re.compile(r'\.[a-zA-Z]+ ?\{[^}]*\}'),  # CSS selectors
        re.compile(r'<[^>]+>'),  # HTML tags
        
        # Other programming languages
        re.compile(r'\bpublic\b|\bstatic\b|\bvoid\b|\bnew\b'),  # Java keywords
        re.compile(r'\bBEGIN\b|\bEND\b'),  # PL/SQL keywords
        re.compile(r'\bSELECT\b|\bFROM\b|\bWHERE\b'),  # SQL keywords
        re.compile(r'\bpackage\b|\buse\b|\bmy\b'),  # Perl keywords
        re.compile(r'\bfunc\b|\bpackage\b'),  # Go keywords
        re.compile(r'\bfn\b|\blet\b|\bmut\b'),  # Rust keywords
        re.compile(r'\bfunc\b|\bvar\b'),  # Swift keywords
        re.compile(r'\bsub\b|\bfunction\b|\bendif\b'),  # VBScript keywords
        re.compile(r'\bif\b|\bthen\b|\belse\b|\bend\b'),  # Basic keywords
        re.compile(r'\bmodule\b|\binclude\b|\bdef\b'),  # Ruby keywords
        re.compile(r'\btemplate\b|\btypename\b'),  # C++ templates
        re.compile(r'\bclass\b|\bextends\b|\bimplements\b'),  # TypeScript keywords
        re.compile(r'\bdef\b|\bdo\b|\bend\b'),  # Ruby keywords
        re.compile(r'\bdata\b|\bwhere\b'),  # Haskell keywords
        re.compile(r'\bnamespace\b|\busing\b'),  # C# keywords
        re.compile(r'\bconst\b|\binterface\b|\bimplements\b'),  # TypeScript keywords
        re.compile(r'\bfn\b|\blet\b|\bmatch\b'),  # Rust keywords
        re.compile(r'\bdef\b|\bclass\b|\bmodule\b'),  # Elixir keywords
        re.compile(r'\bfn\b|\blet\b|\bmod\b'),  # Rust keywords
    ]
    
    # Check for URLs
    if url_pattern.search(text):
        return True
    
    # Check for code snippets
    for pattern in code_patterns:
        if pattern.search(text):
            return True
            
    return False

__all__ = [
    "condition_length_with_tokenizer",
    "condition_non_number_character",
    "condition_min_max_length",
    "condition_not_code_and_link",
]