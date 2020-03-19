import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ArchivedNotesPageComponent } from './archived-notes-page.component';

describe('ArchivedNotesPageComponent', () => {
  let component: ArchivedNotesPageComponent;
  let fixture: ComponentFixture<ArchivedNotesPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ArchivedNotesPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ArchivedNotesPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
