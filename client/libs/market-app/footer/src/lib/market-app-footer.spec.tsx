import { render } from '@testing-library/react';

import MarketAppFooter from './market-app-footer';

describe('MarketAppFooter', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppFooter />);
    expect(baseElement).toBeTruthy();
  });
});
