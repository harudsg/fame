API
===
로그인 및 JWT 발급 절차

1. **로그인**
   - API 엔드포인트: `/login`
   - 메소드: `POST`
   - 요청 예시:
     ```json
     {
       "email": "user@example.com",
       "password": "your_password"
     }
     ```
   - 성공 응답:
     ```json
     {
       "token": "eyJhbGciOiJIUzI1NiIsInR...",
       "expires": "2024-04-12T18:25:43.511Z"
     }
     ```

2. **JWT 발급**
   - 로그인 성공 시, 서버에서 사용자의 인증 정보를 기반으로 JWT를 자동 발급합니다.
   - 이 토큰은 사용자의 권한 및 세션 정보를 포함하며, API 요청 시 Authorization 헤더에 포함해 사용합니다.

3. **토큰 사용**
   - 요청 예시:
     ```
     GET /api/resource
     Authorization: Bearer <your_jwt_token>
     ```

4. **토큰 유효성 및 갱신**
   - JWT는 설정된 만료 시간 후에 유효성을 잃습니다. 서버는 만료 시간을 체크하여, 만료된 토큰에 대해서는 401 Unauthorized 응답을 반환합니다.
   - 리프레시 API 엔드포인트: `/refresh_token`
   - 메소드: `POST`
   - 요청 예시:
     ```json
     {
       "token": "eyJhbGciOiJIUzI1NiIsInR..."
     }
     ```
   - 응답: 새로운 JWT와 만료 시간.
     ```json
     {
       "new_token": "eyJhbGciOiJIUzI1NiIsInR...",
       "expires": "2024-05-12T18:25:43.511Z"
     }
     ```

5. **토큰 만료 및 재발급**
   - 사용자는 만료된 토큰을 리프레시 API를 통해 갱신할 수 있으며, 필요할 경우 다시 로그인하여 새 토큰을 발급받을 수 있습니다.

6. **보안 주의사항**
   - 모든 인증 관련 통신은 HTTPS를 통해 암호화되어야 합니다.
   - 사용자는 토큰을 안전하게 보관하고, 노출되지 않도록 주의해야 합니다.

7. **지원 및 문의**
   - 로그인이나 토큰 발급 및 갱신 과정에서 문제가 발생하거나 추가 지원이 필요한 경우, 지원 팀에 문의하십시오.
