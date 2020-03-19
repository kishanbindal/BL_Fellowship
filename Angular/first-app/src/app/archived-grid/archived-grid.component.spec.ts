import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ArchivedGridComponent } from './archived-grid.component';

describe('ArchivedGridComponent', () => {
  let component: ArchivedGridComponent;
  let fixture: ComponentFixture<ArchivedGridComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ArchivedGridComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ArchivedGridComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
