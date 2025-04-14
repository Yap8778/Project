export interface Diary {
  _id?: string;
  userId: string;
  date: Date;
  mood: string;
  sleepHours: number;
  weather: string;
  content: string;
  image?: string;
  createdAt?: Date;
  updatedAt?: Date;
}
