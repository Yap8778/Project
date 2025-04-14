export interface Consultation {
  _id?: string;
  type: ConsultationType;
  doctorId: string;
  date: Date;
  time: string;
  description: string;
  status: ConsultationStatus;
  userId: string;
}

export type ConsultationType = 'Physical' | 'Virtual';
export type ConsultationStatus = 'Pending' | 'Confirmed' | 'Cancelled';

export interface ConsultationFormData {
  type: ConsultationType;
  doctorId: string;
  date: string;
  time: string;
  description: string;
}

export interface ConsultationResponse {
  success: boolean;
  data?: Consultation | Consultation[];
  error?: string;
  message?: string;
}
