import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-archive-button',
  templateUrl: './archive-button.component.html',
  styleUrls: ['./archive-button.component.css']
})

// <---------Optimization Required!!!!!------------->

export class ArchiveButtonComponent implements OnInit {

  @Output() sendArchive = new EventEmitter()

  is_archived:boolean;

  constructor() { }

  ngOnInit(): void {
    this.is_archived = false
  }

  goArchive(){
    console.log('Is _ archived before : ', this.is_archived)
    this.is_archived = true
    console.log('Is _ archived after : ', this.is_archived)
    this.sendArchive.emit(this.is_archived)
  }

}
