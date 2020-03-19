import { Component, OnInit, Inject } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { FormControl } from '@angular/forms';
import { DataService } from '../services/DataService/data-service.service';
import { Observable } from 'rxjs';
import { startWith, map } from 'rxjs/operators';

@Component({
  selector: 'app-collaborators',
  templateUrl: './collaborators.component.html',
  styleUrls: ['./collaborators.component.css']
})
export class CollaboratorsComponent implements OnInit {

  listOfUsers


  constructor(private dialog: MatDialog, private dataService : DataService) {}

  ngOnInit(): void {
    this.dataService.getAllUsers()
    this.dataService.usersList.subscribe(data => {
      this.listOfUsers = data
      })
    // console.log('All Users List : ', this.listOfCollaborators)
  }

  openCollaboratorDialog(): void{
    const dialogRef = this.dialog.open(CollaboratorsDialogBoxComponent, {
      width: "30rem",
      // height: "12rem",
      data: this.listOfUsers,
      panelClass: 'dialog-container'
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log(result)
      console.log("Collaborators DialogBox Closed!");
    })
  }
}

//CollaboratorsDialogBox

@Component({
  selector: "app-collaborators-dialog-box",
  templateUrl: "collaborators-dialog-box.component.html"
})

export class CollaboratorsDialogBoxComponent implements OnInit{
  
  collaborator_name = new FormControl('');
  host = localStorage.getItem('user').split(',')
  
  filteredOptions : Observable<any>;

  constructor(private dataService : DataService,
    @Inject(MAT_DIALOG_DATA) public data : any){
      // console.log('Data :\n',this.data)
    }

  ngOnInit(){
    console.log('Collaborator name :',this.collaborator_name)
    this.filteredOptions = this.collaborator_name.valueChanges
    .pipe(
      startWith(''),
      map(value => this._filter(value))
    );
  }

  getDataUsername(user){
    return user.username
  }

  _filter(value: string): string[] {
    const filterValue = value.toLowerCase()
    console.log('Data :\n', this.data)
    return this.data.filter(option => option.username.toLowerCase().includes(filterValue));
  }

}
