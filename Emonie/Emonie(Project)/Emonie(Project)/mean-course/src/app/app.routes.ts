import { Routes } from '@angular/router';

export const routes: Routes = [
  { path: 'auth', loadChildren: () => import('./auth/auth.module').then(m => m.AuthModule) },
  { path: '', redirectTo: 'auth/login', pathMatch: 'full' },
  { path: 'diary', loadChildren: () => import('./Diary/diary.module').then(m => m.DiaryModule) },
  { path: 'todo', loadChildren: () => import('./To-do list/todo.module').then(m => m.TodoModule) },
  { path: 'consultations', loadChildren: () => import('./Consultation/consultation.module').then(m => m.ConsultationModule) }
];
