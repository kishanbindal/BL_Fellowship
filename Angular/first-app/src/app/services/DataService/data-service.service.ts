import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { formattedError } from '@angular/compiler';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class DataService{

  private responseSource = new BehaviorSubject('No Notes to Show');
  public cast = this.responseSource.asObservable();

  private reminderSource = new BehaviorSubject('No Notes with reminders');
  public reminderNotes = this.reminderSource.asObservable();

  private archivedSource = new BehaviorSubject('No Archived Notes');
  public archivedNotes = this.archivedSource.asObservable();

  private labelSource = new BehaviorSubject('No labels to show');
  public labelData = this.labelSource.asObservable();

  private userSource = new BehaviorSubject('No Users');
  public usersList = this.userSource.asObservable();

  private searchSource = new BehaviorSubject('No Notes');
  public searchNotes = this.searchSource.asObservable();

  constructor(private http: HttpClient, private snackbar: MatSnackBar,
    private router: Router) { }

  //-----------Users Related-----------------------------

  getAllUsers(){
    let token = localStorage.getItem('token')
    return this.http.get('http://localhost:8000/fun/api/users', {headers : {
      'token': token,
    }}).subscribe(response => {
      if (response['success'] === true){
        let data = response['data']
        this.userSource.next(data)
      }
    })
  }

  uploadProfilePicture(image_file){
    let token = localStorage.getItem('token')
    console.log('sending profile_image to backend');
    let formData = new FormData()
    formData.append('profile_image', image_file)
    
    return this.http.post('http://localhost:8000/fun/api/uploadimage', formData, {headers :{
      // "Content-Type": "multipart/form-data",
      'token': token,
      // "Accept": "multipart/form-data"
    }})
  }

  //-----------Note Related Options--------------------------
  getAllNotes(){
    let token = localStorage.getItem('token') 
    return this.http.get('http://localhost:8000/notes/api/notes/', {headers:{
      "Content-Type": "application/json",
      "token": token,
    }}).subscribe((response) =>{
      if(response['success']===true){
        let data = response['data']
        console.log('Incoming Note Data: \n', data)
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

  getArchivedNotes(){
    let token = localStorage.getItem('token')
    // console.log('archived token : ', token)
    this.http.get('http://localhost:8000/notes/api/archived', { headers :{
      'token': token
    }}).subscribe(response => {
      // console.log('response from Api: ', response);
      if (response['success'] === true){
        let archived_data  = response['data'];
        this.archivedSource.next(archived_data);
      }
    })
  }

  updateNote(note_data){
    let token = localStorage.getItem('token');
    return this.http.patch(`http://localhost:8000/notes/api/notes/${note_data.id}`, note_data, { headers:{
      'token': token
    }})
  }

  getSearchedNote(note_data){
    let token = localStorage.getItem('token')
    this.http.post('http://localhost:8000/notes/api/search/', note_data, {headers:{
      'token': token
    }}).subscribe(response => {
      if (response['success']===true){
        let searchNoteData= response['data']
        console.log(searchNoteData)
        this.searchSource.next(searchNoteData)
        this.router.navigate(['/search'])
      }
    })
  }

  //---------------Label related Operations-----------------------------
  postLabel(label_data){
    let token = localStorage.getItem('token')
    return this.http.post('http://localhost:8000/notes/api/labels/', label_data, {headers: {
      'token': token
    }})
  }

  getLabels(){
    let token = localStorage.getItem('token');
    this.http.get('http://localhost:8000/notes/api/labels', {headers: {
      'token': token
    }})
    .subscribe(response => {
      // console.log('Labels Data Service : ', response)
      if(response['success'] === true){
        let label = response['data']
        // console.log('Label Data : ',label)
        this.labelSource.next(label);
      }else{
        console.log(response['message']);
      } 
    })
  }

  deleteLabelId(label_id:number){
    let token = localStorage.getItem('token')
    return this.http.delete(`http://localhost:8000/notes/api/labels/${label_id}`, {headers:{
      'token': token
    }})
  }

  updateLabelId(label){
    let token = localStorage.getItem('token')
    return this.http.put(`http://localhost:8000/notes/api/labels/${label.id}`, label , {headers : {
      'token': token
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