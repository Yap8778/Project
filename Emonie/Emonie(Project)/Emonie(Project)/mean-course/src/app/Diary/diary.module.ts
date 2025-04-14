import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { DiaryComponent } from './diary.component';
import { DiaryRoutingModule } from './diary-routing.module';

@NgModule({
  declarations: [
    DiaryComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    DiaryRoutingModule
  ]
})
export class DiaryModule { } 