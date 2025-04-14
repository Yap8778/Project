import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { Register } from './register.model';
import { environment } from '@environments/environment';

@Injectable({
  providedIn: 'root'
})
export class RegisterService {
  private apiUrl = `${environment.apiUrl}/auth/register`;

  constructor(private http: HttpClient) { }

  validateUsername(username: string): boolean {
    // Username validation rules
    const usernameRegex = /^[a-zA-Z0-9_]{3,20}$/;
    return usernameRegex.test(username);
  }

  validatePassword(password: string): boolean {
    // Password validation rules
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$/;
    return passwordRegex.test(password);
  }

  validateEmail(email: string): boolean {
    // Email validation rules
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  private handleError(error: HttpErrorResponse) {
    let errorMessage = 'An error occurred during registration';
    
    if (error.error instanceof ErrorEvent) {
      // Client-side error
      errorMessage = error.error.message;
    } else {
      // Server-side error
      switch (error.status) {
        case 400:
          errorMessage = 'Invalid registration data';
          break;
        case 409:
          errorMessage = 'Username or email already exists';
          break;
        case 500:
          errorMessage = 'Server error occurred';
          break;
        default:
          errorMessage = error.error.message || 'Registration failed';
      }
    }
    
    return throwError(() => new Error(errorMessage));
  }

  register(user: Register): Observable<any> {
    // Validate user data before sending
    if (!this.validateUsername(user.username)) {
      return throwError(() => new Error('Invalid username format'));
    }
    if (!this.validateEmail(user.email)) {
      return throwError(() => new Error('Invalid email format'));
    }
    if (!this.validatePassword(user.password)) {
      return throwError(() => new Error('Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character'));
    }
    if (user.password !== user.confirmPassword) {
      return throwError(() => new Error('Passwords do not match'));
    }

    return this.http.post(this.apiUrl, user).pipe(
      map(response => {
        return {
          success: true,
          data: response
        };
      }),
      catchError(this.handleError)
    );
  }
}
