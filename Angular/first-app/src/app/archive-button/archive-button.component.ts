import { Component, OnInit, Output, EventEmitter, Input } from '@angular/core';

@Component({
  selector: 'app-archive-button',
  templateUrl: './archive-button.component.html',
  styleUrls: ['./archive-button.component.css']
})

// <---------Optimization Required!!!!!------------->

export class ArchiveButtonComponent implements OnInit {

  @Output() sendArchive = new EventEmitter()

  @Output() crudArchiveEmitter = new EventEmitter()

  @Input() archivedStatus

  is_archived:boolean;

  constructor() { }

  ngOnInit(): void {
    this.is_archived = this.archivedStatus
  }

  goArchive(){
    if (this.is_archived === false || this.archivedStatus === false){
      // console.log('Is _ archived before : ', this.is_archived)
      console.log('archived Status  : ' ,this.archivedStatus)
    this.is_archived = true
    this.archivedStatus = true
    // console.log('Is _ archived after : ', this.is_archived)
    }else{
      this.is_archived = false;
      this.archivedStatus = true;
    }
    this.sendArchive.emit(this.is_archived)
    this.crudArchiveEmitter.emit(this.archivedStatus)
  }

  // crudArchive(){
  //   if (this.archivedStatus === true){
  //     this.archivedStatus = false;
  //     this.crudArchiveEmitter.emit(this.archivedStatus)
  //     this.sendArchive.emit(this.archivedStatus);
  //   }else{
  //     this.crudArchiveEmitter.emit(this.archivedStatus=true);
  //   }
  // }

}
