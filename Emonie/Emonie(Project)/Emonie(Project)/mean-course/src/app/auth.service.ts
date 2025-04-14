import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface RegisterResponse {
  message: string;
  user: {
    id: string;
    username: string;
    email: string;
  };
}

export interface ErrorResponse {
  error: {
    message: string;
  };
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:3000/api/auth';

  constructor(private http: HttpClient) {}

  register(username: string, email: string, password: string): Observable<RegisterResponse> {
    const body = { username, email, password };
    console.log('Sending registration request:', body);
    return this.http.post<RegisterResponse>(`${this.apiUrl}/register`, body);
  }
}