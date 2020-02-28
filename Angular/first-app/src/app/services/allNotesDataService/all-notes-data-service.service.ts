import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AllNotesDataService{

  private responseSource = new BehaviorSubject('No Notes to Show');
  public cast = this.responseSource.asObservable();

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
}

// console.log(`Server response :${response}`)
//       if (response['success'] === true){
//         // console.log(response)
//         return this.responseSource.next(response['data']);
//       }else{
//         console.log('Some Issue Occured')
//       }