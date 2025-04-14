import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { RegisterComponent } from './app/auth/Register/register.component';

bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient(),
    provideRouter([
      { path: 'register', component: RegisterComponent },
      { path: 'login', component: RegisterComponent }, // Replace with actual login component when created
      { path: '', redirectTo: '/register', pathMatch: 'full' }
    ])
  ]
}).catch(err => console.error(err));
