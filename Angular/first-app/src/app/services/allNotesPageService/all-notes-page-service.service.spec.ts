import { TestBed } from '@angular/core/testing';

import { AllNotesPageServiceService } from './all-notes-page-service.service';

describe('AllNotesPageServiceService', () => {
  let service: AllNotesPageServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AllNotesPageServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
