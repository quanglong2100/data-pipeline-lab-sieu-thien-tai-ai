def run_semantic_checks(doc_dict: dict) -> bool:
    content = doc_dict.get("content", "")
    
    # 1. Kiểm tra độ dài: Nếu content trống hoặc < 10 ký tự -> Loại
    if not content or len(content) < 10:
        return False
    
    # 2. Kiểm tra từ khóa lỗi (Toxic/Corrupt content)
    toxic_keywords = ["Null pointer exception", "OCR Error", "Traceback"]
    for word in toxic_keywords:
        if word.lower() in content.lower():
            return False
            
    return True