import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchNotesPageComponent } from './search-notes-page.component';

describe('SearchNotesPageComponent', () => {
  let component: SearchNotesPageComponent;
  let fixture: ComponentFixture<SearchNotesPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SearchNotesPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchNotesPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
