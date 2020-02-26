import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Note } from 'src/app/note';

@Injectable({
  providedIn: 'root'
})
export class AllNotesPageService{

  constructor(private http: HttpClient) { }

  getAllNotes(): Observable<Note[]>{
    let token = localStorage.getItem('token')
    let result = null; 
    return this.http.get<Note[]>('http://localhost:8000/notes/api/notes/', {headers:{
      "Content-Type": "application/json",
      "token": token,
    }})
    
  }
}

// .subscribe((response) => {
//   if (response['success'] === true){
//     console.log(response['data'])
//   }else{
//     console.log("Unsuccessful in retrieving data from Server");
//   }
// });
