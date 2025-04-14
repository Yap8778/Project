import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthService } from './auth/auth.service';

const routes: Routes = [
  { path: 'login', loadChildren: () => import('./auth/auth.module').then(m => m.AuthModule) },
  { 
    path: '', 
    loadChildren: () => import('./Index Page/index.module').then(m => m.IndexModule),
    canActivate: [AuthService]
  },
  { 
    path: 'diary', 
    loadChildren: () => import('./Diary/diary.module').then(m => m.DiaryModule),
    canActivate: [AuthService]
  },
  { 
    path: 'todo', 
    loadChildren: () => import('./To-do list/todo.module').then(m => m.TodoModule),
    canActivate: [AuthService]
  },
  { 
    path: 'consultation', 
    loadChildren: () => import('./Consultation/consultation.module').then(m => m.ConsultationModule),
    canActivate: [AuthService]
  },
  { path: '**', redirectTo: '' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { } 