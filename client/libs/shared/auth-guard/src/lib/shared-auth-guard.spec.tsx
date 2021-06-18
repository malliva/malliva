import { render } from '@testing-library/react';

import SharedAuthGuard from './shared-auth-guard';

describe('SharedAuthGuard', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<SharedAuthGuard />);
    expect(baseElement).toBeTruthy();
  });
});
