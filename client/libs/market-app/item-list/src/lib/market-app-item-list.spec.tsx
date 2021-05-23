import { render } from '@testing-library/react';

import MarketAppItemList from './market-app-item-list';

describe('MarketAppItemList', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppItemList />);
    expect(baseElement).toBeTruthy();
  });
});
