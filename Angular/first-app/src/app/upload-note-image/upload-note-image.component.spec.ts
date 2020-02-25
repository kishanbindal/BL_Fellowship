import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UploadNoteImageComponent } from './upload-note-image.component';

describe('UploadNoteImageComponent', () => {
  let component: UploadNoteImageComponent;
  let fixture: ComponentFixture<UploadNoteImageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UploadNoteImageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UploadNoteImageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
