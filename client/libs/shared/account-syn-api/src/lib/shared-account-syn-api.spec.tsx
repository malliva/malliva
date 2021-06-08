import { render } from '@testing-library/react';

import SharedAccountSynApi from './shared-account-syn-api';

describe('SharedAccountSynApi', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<SharedAccountSynApi />);
    expect(baseElement).toBeTruthy();
  });
});
