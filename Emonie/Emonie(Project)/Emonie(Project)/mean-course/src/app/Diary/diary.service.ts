import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Diary } from './diary.model';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class DiaryService {
  private apiUrl = `${environment.apiUrl}/diaries`;

  constructor(private http: HttpClient) { }

  getDiaries(): Observable<Diary[]> {
    return this.http.get<Diary[]>(this.apiUrl);
  }

  getDiary(id: string): Observable<Diary> {
    return this.http.get<Diary>(`${this.apiUrl}/${id}`);
  }

  createDiary(diary: FormData): Observable<Diary> {
    return this.http.post<Diary>(this.apiUrl, diary);
  }

  updateDiary(id: string, diary: FormData): Observable<Diary> {
    return this.http.put<Diary>(`${this.apiUrl}/${id}`, diary);
  }

  deleteDiary(id: string): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }

  uploadImage(image: File): Observable<{ url: string }> {
    const formData = new FormData();
    formData.append('image', image);
    return this.http.post<{ url: string }>(`${this.apiUrl}/upload`, formData);
  }
}
