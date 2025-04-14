import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { TodoService } from './todo.service';
import { Todo } from './todo.model';

@Component({
  selector: 'app-todo',
  templateUrl: './todo.component.html',
  styleUrls: ['./todo.component.css']
})
export class TodoComponent implements OnInit {
  todos: Todo[] = [];
  todoForm: FormGroup;
  newTodoTitle = '';

  constructor(
    private todoService: TodoService,
    private fb: FormBuilder
  ) {
    this.todoForm = this.fb.group({
      title: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    this.loadTodos();
  }

  loadTodos(): void {
    this.todoService.getTodos().subscribe(
      todos => this.todos = todos,
      error => console.error('Error loading todos:', error)
    );
  }

  addTodo(): void {
    if (this.newTodoTitle.trim()) {
      const newTodo: Todo = {
        title: this.newTodoTitle.trim(),
        completed: false,
        createdAt: new Date(),
        userId: 'current-user-id' // Replace with actual user ID from auth service
      };

      this.todoService.createTodo(newTodo).subscribe(
        () => {
          this.newTodoTitle = '';
          this.loadTodos();
        },
        error => console.error('Error creating todo:', error)
      );
    }
  }

  toggleTodo(todo: Todo): void {
    todo.completed = !todo.completed;
    this.todoService.updateTodo(todo._id as string, todo).subscribe(
      () => this.loadTodos(),
      error => console.error('Error updating todo:', error)
    );
  }

  deleteTodo(id: string): void {
    this.todoService.deleteTodo(id).subscribe(
      () => this.loadTodos(),
      error => console.error('Error deleting todo:', error)
    );
  }
}
