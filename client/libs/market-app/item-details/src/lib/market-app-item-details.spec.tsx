import { render } from '@testing-library/react';

import MarketAppItemDetails from './market-app-item-details';

describe('MarketAppItemDetails', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppItemDetails />);
    expect(baseElement).toBeTruthy();
  });
});
