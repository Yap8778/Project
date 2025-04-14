import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IndexData } from './index.model';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class IndexService {
  private apiUrl = `${environment.apiUrl}/diaries`;

  constructor(private http: HttpClient) { }

  getPublicDiaries(): Observable<IndexData[]> {
    return this.http.get<IndexData[]>(`${this.apiUrl}/public`);
  }
}
