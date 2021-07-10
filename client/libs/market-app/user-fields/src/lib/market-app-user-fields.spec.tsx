import { render } from '@testing-library/react';

import MarketAppUserFields from './market-app-user-fields';

describe('MarketAppUserFields', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppUserFields />);
    expect(baseElement).toBeTruthy();
  });
});
