List of lecture files

**오류 및 경고 헤결 방법**
SSLCertificate 오류가 발생할 때의 처치 방법 [SSL: CERTIFICATE_VERIFY_FAILED]
https://www.mongodb.com/community/forums/t/keep-getting-serverselectiontimeouterror/126190/12 에 기술된 방법임.
1. Download https://letsencrypt.org/certs/lets-encrypt-r3.pem 
2. rename file .pem to .cer (파일 확장자 수정)
3. double click and install (더블클릭해서 인증서 설치)
이렇게 인증서를 설치하면 SSL 관련 문제는 해결됨.

RequestsDependencyWarning: urllib3 (1.26.6) or chardet (5.1.0)/charset_normalizer (2.0.4) doesn't match a supported version! 문제 해결 방법
```pip install --upgrade requests```

**Jupyter Kernel 관련 명령**

Juputer Kernal 목록 보기
```jupyter kernelspec list```

Jupyter kernel 설치
```ipython kernel install --name "opencv" --user```

Jupyter kernal 삭제
```jupyter kernelspec remove opencv```
