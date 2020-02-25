import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NoteSettingComponent } from './note-setting.component';

describe('NoteSettingComponent', () => {
  let component: NoteSettingComponent;
  let fixture: ComponentFixture<NoteSettingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NoteSettingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NoteSettingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
