import { render } from '@testing-library/react';

import MarketAppUserRights from './market-app-user-rights';

describe('MarketAppUserRights', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppUserRights />);
    expect(baseElement).toBeTruthy();
  });
});
