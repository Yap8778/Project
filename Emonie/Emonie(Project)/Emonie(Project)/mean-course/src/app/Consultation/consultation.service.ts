import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Consultation } from './consultation.model';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ConsultationService {
  private apiUrl = `${environment.apiUrl}/consultations`;

  constructor(private http: HttpClient) { }

  getConsultations(): Observable<Consultation[]> {
    return this.http.get<Consultation[]>(this.apiUrl);
  }

  createConsultation(consultation: Consultation): Observable<Consultation> {
    return this.http.post<Consultation>(this.apiUrl, consultation);
  }

  updateConsultation(id: string, consultation: Consultation): Observable<Consultation> {
    return this.http.put<Consultation>(`${this.apiUrl}/${id}`, consultation);
  }

  deleteConsultation(id: string): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}
