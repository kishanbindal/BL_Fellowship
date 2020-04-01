import { Component, OnInit, Inject, Output, EventEmitter } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { FormControl, FormArray, FormGroup } from '@angular/forms';
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

  @Output() sendCollaborators = new EventEmitter(false)


  constructor(private dialog: MatDialog, private dataService : DataService) {}

  ngOnInit(): void {
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
      this.listOfUsers = result;
      console.log(this.listOfUsers)
      this.sendCollaborators.emit(this.listOfUsers);
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
  listOfCollaborators = [];
  host = localStorage.getItem('user').split(',')

  // collab_data = new FormGroup({
  //   id : new FormControl(''),
  //   username: new FormControl(''),
  //   email: new FormControl(''),
  //   profileImage: new FormControl(''),
  // })
  
  filteredOptions : Observable<any>;

  constructor(private dataService : DataService,
    public dialogRef : MatDialogRef<CollaboratorsDialogBoxComponent>,
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
    return this.data.filter(option => option.username.toLowerCase().includes(filterValue));
  }

  addCollab(collabName){  

    for (let obj of this.data){
      if (this.collaborator_name.value === obj.username){
        // console.log('Collaborator : ', obj)
        this.listOfCollaborators.push(obj);
        console.log('listOf Collaborators: ', this.listOfCollaborators)
      }
    }
    // collabName.setValue(collabName.username)
    console.log('List Of Collaborators : ', this.listOfCollaborators);
    this.collaborator_name.setValue('');
  }

  onSave(){
    console.log('Closing Collab Dialog and sending data to main component');
    this.dialogRef.close(this.listOfCollaborators)
  }

}
