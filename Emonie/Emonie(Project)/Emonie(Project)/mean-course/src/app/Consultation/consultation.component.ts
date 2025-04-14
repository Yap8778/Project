import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ConsultationService } from './consultation.service';
import { Consultation, ConsultationFormData, ConsultationStatus } from './consultation.model';
import { AuthService } from '../auth/auth.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-consultation',
  templateUrl: './consultation.component.html',
  styleUrls: ['./consultation.component.css']
})
export class ConsultationComponent implements OnInit, OnDestroy {
  consultationForm: FormGroup;
  consultations: Consultation[] = [];
  isEditing = false;
  selectedConsultation: Consultation | null = null;
  errorMessage: string | null = null;
  loading = false;
  private subscriptions: Subscription[] = [];

  constructor(
    private fb: FormBuilder,
    private consultationService: ConsultationService,
    private authService: AuthService
  ) {
    this.consultationForm = this.fb.group({
      type: ['', [Validators.required]],
      doctorId: ['', [Validators.required]],
      date: ['', [Validators.required]],
      time: ['', [Validators.required]],
      description: ['', [Validators.required]]
    });
  }

  ngOnInit(): void {
    this.loadConsultations();
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => sub.unsubscribe());
  }

  loadConsultations(): void {
    this.loading = true;
    this.errorMessage = null;
    
    const sub = this.consultationService.getConsultations().subscribe({
      next: (consultations) => {
        this.consultations = consultations;
        this.loading = false;
      },
      error: (error) => {
        console.error('Error loading consultations:', error);
        this.errorMessage = error.message || 'Failed to load consultations. Please try again later.';
        this.loading = false;
      }
    });
    
    this.subscriptions.push(sub);
  }

  onSubmit(): void {
    if (this.consultationForm.invalid) {
      this.errorMessage = 'Please fill in all required fields.';
      return;
    }

    const formValue = this.consultationForm.value as ConsultationFormData;
    const currentUser = this.authService.getCurrentUser();
    
    if (!currentUser) {
      this.errorMessage = 'User not authenticated. Please log in.';
      return;
    }

    this.loading = true;
    this.errorMessage = null;

    const consultation: Omit<Consultation, '_id'> = {
      ...formValue,
      date: new Date(formValue.date),
      status: 'Pending' as ConsultationStatus,
      userId: currentUser.user._id
    };

    const observable = this.isEditing && this.selectedConsultation
      ? this.consultationService.updateConsultation(this.selectedConsultation._id as string, consultation)
      : this.consultationService.createConsultation(consultation);

    const sub = observable.subscribe({
      next: () => {
        this.resetForm();
        this.loadConsultations();
        this.loading = false;
      },
      error: (error) => {
        console.error('Error saving consultation:', error);
        this.errorMessage = error.message || 'Failed to save consultation. Please try again later.';
        this.loading = false;
      }
    });

    this.subscriptions.push(sub);
  }

  editConsultation(consultation: Consultation): void {
    this.isEditing = true;
    this.selectedConsultation = consultation;
    this.consultationForm.patchValue({
      ...consultation,
      date: typeof consultation.date === 'string' 
        ? consultation.date 
        : consultation.date.toISOString().split('T')[0]
    });
    this.errorMessage = null;
  }

  deleteConsultation(id: string): void {
    if (confirm('Are you sure you want to delete this consultation?')) {
      this.loading = true;
      this.errorMessage = null;

      const sub = this.consultationService.deleteConsultation(id).subscribe({
        next: () => {
          this.loadConsultations();
          this.loading = false;
        },
        error: (error) => {
          console.error('Error deleting consultation:', error);
          this.errorMessage = error.message || 'Failed to delete consultation. Please try again later.';
          this.loading = false;
        }
      });

      this.subscriptions.push(sub);
    }
  }

  resetForm(): void {
    this.consultationForm.reset();
    this.isEditing = false;
    this.selectedConsultation = null;
    this.errorMessage = null;
  }
}
