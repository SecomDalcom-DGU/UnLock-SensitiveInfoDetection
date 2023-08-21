import re
import PyPDF2
import sys

# parameter
docName = sys.argv[1]

def sensitive_info_detection(text):
    # 휴대폰 번호 패턴을 정규 표현식으로 정의합니다
    phone_pattern = r'\b(?:010-\d{4}-\d{4}|\d{11})\b'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    rnn_pattern = r'\b\d{6}-[1-4]\d{6}\b'  # 주민등록번호 패턴 (앞 6자리-뒷 7자리)


    phone_numbers = re.findall(phone_pattern, text)
    email_addresses = re.findall(email_pattern, text)
    rnn_numbers = re.findall(rnn_pattern, text)
    
    return phone_numbers, email_addresses, rnn_numbers




if __name__ == "__main__":
    # PDF 파일을 열어 텍스트를 추출
    pdf_file_path = docName
    
    pdf_text = ''
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()

    # 추출한 텍스트에서 민감정보 감지
    phone_numbers, email_addresses, rnn_numbers = sensitive_info_detection(pdf_text)


    if phone_numbers:
        print("파일에서 발견된 휴대폰 번호:")
        for number in phone_numbers:
            print(number)

    if email_addresses:
        print("파일에서 발견된 이메일 주소:")
        for email in email_addresses:
            print(email)

    if rnn_numbers:
        print("파일에서 발견된 주민등록번호:")
        for rnn in rnn_numbers:
            print(rnn)

    if not phone_numbers and not email_addresses:
        print("파일에서 민감 정보를 찾지 못했습니다.")

