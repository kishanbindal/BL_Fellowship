import { Directive, Output, EventEmitter, HostBinding, HostListener } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';

@Directive({
  selector: '[appDragDrop]'
})
export class DragDropDirective {

  @Output() onFileDrop= new EventEmitter(false);

  @HostBinding("style.background") private background = "#eee";

  imgFile
  imgUrl

  constructor(private domSanitizer : DomSanitizer){}

  @HostListener("dragleave", ['$event']) public onDragLeave(evt: DragEvent){

    evt.preventDefault();
    evt.stopPropagation();
    this.background = '#eee';
  }

  @HostListener("dragover", ['$event']) public onDragOver(evt: DragEvent){
    evt.preventDefault();
    evt.stopPropagation();
    this.background= '#999';
  }

  @HostListener('drop', ['$event']) public onDrop(evt: DragEvent){
    evt.preventDefault();
    evt.stopPropagation();

    let file = evt.dataTransfer.files;

    if (file.length > 0){
      this.imgFile = file[0];
      let reader = new FileReader();
      reader.readAsDataURL(this.imgFile)
      setTimeout(()=>{
        console.log(reader.result);
        this.imgUrl = reader.result
        this.imgUrl = this.domSanitizer.bypassSecurityTrustUrl(this.imgUrl);
        this.onFileDrop.emit({'file': this.imgFile, 'url': this.imgUrl})
      }, 100)
      
    }
  }

}
