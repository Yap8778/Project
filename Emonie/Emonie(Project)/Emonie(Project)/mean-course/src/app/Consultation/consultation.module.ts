import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { ConsultationComponent } from './consultation.component';
import { ConsultationRoutingModule } from './consultation-routing.module';
import { ConsultationService } from './consultation.service';

@NgModule({
  declarations: [
    ConsultationComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    FormsModule,
    ConsultationRoutingModule
  ],
  providers: [ConsultationService]
})
export class ConsultationModule { } 