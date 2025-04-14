import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { DiaryService } from './diary.service';
import { Diary } from './diary.model';

@Component({
  selector: 'app-diary',
  templateUrl: './diary.component.html',
  styleUrls: ['./diary.component.css']
})
export class DiaryComponent implements OnInit {
  diaries: Diary[] = [];
  diaryForm: FormGroup;
  isEditing = false;
  selectedDiary: Diary | null = null;
  selectedFile: File | null = null;

  constructor(
    private diaryService: DiaryService,
    private fb: FormBuilder
  ) {
    this.diaryForm = this.fb.group({
      date: ['', Validators.required],
      mood: ['', Validators.required],
      sleepHours: ['', [Validators.required, Validators.min(0), Validators.max(24)]],
      weather: ['', Validators.required],
      content: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    this.loadDiaries();
  }

  loadDiaries(): void {
    this.diaryService.getDiaries().subscribe(
      diaries => this.diaries = diaries,
      error => console.error('Error loading diaries:', error)
    );
  }

  onFileSelected(event: any): void {
    this.selectedFile = event.target.files[0];
  }

  onSubmit(): void {
    if (this.diaryForm.invalid) return;

    const formData = new FormData();
    const formValue = this.diaryForm.value;

    Object.keys(formValue).forEach(key => {
      formData.append(key, formValue[key]);
    });

    if (this.selectedFile) {
      formData.append('image', this.selectedFile);
    }

    if (this.isEditing && this.selectedDiary) {
      this.diaryService.updateDiary(this.selectedDiary._id as string, formData).subscribe(
        () => {
          this.resetForm();
          this.loadDiaries();
        },
        error => console.error('Error updating diary:', error)
      );
    } else {
      this.diaryService.createDiary(formData).subscribe(
        () => {
          this.resetForm();
          this.loadDiaries();
        },
        error => console.error('Error creating diary:', error)
      );
    }
  }

  editDiary(diary: Diary): void {
    this.isEditing = true;
    this.selectedDiary = diary;
    this.diaryForm.patchValue({
      date: diary.date,
      mood: diary.mood,
      sleepHours: diary.sleepHours,
      weather: diary.weather,
      content: diary.content
    });
  }

  deleteDiary(id: string): void {
    if (confirm('Are you sure you want to delete this diary entry?')) {
      this.diaryService.deleteDiary(id).subscribe(
        () => this.loadDiaries(),
        error => console.error('Error deleting diary:', error)
      );
    }
  }

  resetForm(): void {
    this.diaryForm.reset();
    this.isEditing = false;
    this.selectedDiary = null;
    this.selectedFile = null;
  }
}
