import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService{

  private responseSource = new BehaviorSubject('No Notes to Show');
  public cast = this.responseSource.asObservable();

  private reminderSource = new BehaviorSubject('No Notes with reminders');
  public reminderNotes = this.reminderSource.asObservable();

  constructor(private http: HttpClient) { }

  getAllNotes(){
    let token = localStorage.getItem('token') 
    return this.http.get('http://localhost:8000/notes/api/notes/', {headers:{
      "Content-Type": "application/json",
      "token": token,
    }}).subscribe((response) =>{
      if(response['success']===true){
        let data = response['data']
        this.responseSource.next(data)
      }
    })
  }

  getReminderNotes(){
    let token = localStorage.getItem('token');
    console.log('Getting notes with Reminders.')
    return this.http.get('http://localhost:8000/notes/api/reminder',{headers:{
      // 'Content-type': 'application/json',
      'token': token,
    }}).subscribe((response) => {
      if(response['success'] === true){
        let reminder_data = response['data']
        this.reminderSource.next(reminder_data)
      }
    })
  }

  postNote(note_data:object){
    let token = localStorage.getItem('token');
    return this.http.post('http://localhost:8000/notes/api/notes/', note_data, {headers:{
      'token': token,
    }})
  }

}

// console.log(`Server response :${response}`)
//       if (response['success'] === true){
//         // console.log(response)
//         return this.responseSource.next(response['data']);
//       }else{
//         console.log('Some Issue Occured')
//       }