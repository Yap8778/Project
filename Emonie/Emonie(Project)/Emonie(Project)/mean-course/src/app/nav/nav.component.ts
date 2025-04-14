import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth/auth.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent {
  constructor(
    public authService: AuthService,
    private router: Router
  ) {}

  logout(): void {
    localStorage.removeItem('currentUser');
    this.router.navigate(['/login']);
  }
} 