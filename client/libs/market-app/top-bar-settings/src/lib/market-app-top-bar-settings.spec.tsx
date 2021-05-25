import { render } from '@testing-library/react';

import MarketAppTopBarSettings from './market-app-top-bar-settings';

describe('MarketAppTopBarSettings', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppTopBarSettings />);
    expect(baseElement).toBeTruthy();
  });
});
