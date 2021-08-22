import { render } from '@testing-library/react';

import MarketAppCreateListing from './market-app-create-listing';

describe('MarketAppCreateListing', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppCreateListing />);
    expect(baseElement).toBeTruthy();
  });
});
