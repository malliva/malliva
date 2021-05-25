import { render } from '@testing-library/react';

import MarketAppTopBanner from './market-app-top-banner';

describe('MarketAppTopBanner', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppTopBanner />);
    expect(baseElement).toBeTruthy();
  });
});
